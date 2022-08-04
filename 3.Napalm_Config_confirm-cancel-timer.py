#device.commit_config(revert_in=X) = Commit in X seconds
#device.confirm_commit() = User confirms to commit
#device.rollback() = Immediately rollback changes
#device.has_pending_commit() = If there is any commit pending for user to confirm

from napalm import get_network_driver
driver = get_network_driver('ios')

#Using context manager to automatically open and close the connection to the device
with driver(hostname='10.10.20.48',username='developer', password='C1sco12345',optional_args={'port':22}) as device:

    #here config is used instead of specifying filename
    #In this example, config change will be rolled backed and not saved(committed)
    device.load_merge_candidate(config="hostname CISCO")
    print(device.compare_config())
    device.commit_config(revert_in=60) # Revert in 60 seconds if not commited
    print(device.has_pending_commit()) # Is there any changes that is waiting to be committed?
    device.rollback() # Rollback the change
    print(device.has_pending_commit()) # Now there shouldn't be change pending commits
    
    #In this example, we will let the timer expire, by the end the config will rolledback without user intervention
    device.load_merge_candidate(config="hostname CISCO")
    print(device.compare_config())
    device.commit_config(revert_in=60) # Revert the changes in 60 seconds
    print(device.has_pending_commit())
    #Let the timer expire
    print(device.has_pending_commit())
    
    #In this example, we will confirm commit before timer expires
    device.load_merge_candidate(config="hostname CISCO")
    print(device.compare_config())
    device.commit_config(revert_in=60)
    print(device.has_pending_commit())
    device.confirm_commit()
    print(device.has_pending_commit())





