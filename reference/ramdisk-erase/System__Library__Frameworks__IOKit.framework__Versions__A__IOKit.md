# `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 1,413,840 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 25 (Size: 3784)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (7)

- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libenergytrace.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.12)`
- `/usr/lib/libbsm.0.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (7 classes, 0 protocols)

Classes: `HIDConnection`, `HIDDevice`, `HIDElement`, `HIDEvent`, `HIDEventService`, `HIDServiceClient`, `HIDSession`

## Strings (2,636)

First 2,500 of 2,636.
```
IOObjectRetain:0x%x
bootstrap_check_in() failed: %s
Found timeout %@ for category string %@
Released assertion id gCurrentRemoteAssertion: 0x%x: 0x%x.Logging everything to powerd %@ %ld
Not a dictianary for 0x%x
0x%llx: close completed
Invalid reply from PowerD\n
HIDVS (id:%llx) invalid parameters
Set cursor bounds minx:%d miny:%d maxx:%d maxy:%d
Service: %@ trigger matching failed: service is already registered
%s: iohideventsystem_client_dispatch_event_filter:0x%x
Not a dictinary for 0x%x
IOCreatePlugInInterfaceForService:0x%x for serviceID:%#llx
assertion failure: \"retainCount\" -> %llu
IOHIDEventSystem - enumeration queue termination
IOHIDEventSystem TCC matching: could not load TCC.framework, gating disabled
%@ is not serializable. result: %@
%s: HIDVS ID:%llx destroy
Received assertion activity update refcnt %u overflow %d
IOServiceAddMatchingNotification:0x%x
Received termination imminent error for connection 0x%lx
Initial level is off for 0x%x: %@
IOPMUnregisterNotification: no valid ref for 0x%lx
HIDVS (id: %llx) invalid event data
%s: iohideventsystem_client_dispatch_properties_changed:0x%x
%s: iohideventsystem_client_dispatch_client_records_changed:0x%x
assertion failure: \"pthread_mutex_init(&service->queueContext->lock, &mutexattr)\" -> %llu
__IOHIDServiceLoadObjcServicePlugin failed to find symbol %@ for bundle %@
Failed to find %s for set, switch to default CFPreferences
unexpected policy request %llu
%@
assertion failure: \"pthread_mutex_lock(&(session->queueContext)->lock)\" -> %llu
Powerd has requested assertion activity update
io_hideventsystem_create_virtual_service :%x
HIDVS (id: %llx) does not exist
EventForClient filtered type:%d sender:0x%llx eventInfo:(%@) service filter:%@ for client:%@
%s: Event latency:%lld type:%d sender:0x%llx
mach_port_deallocate(server_port) %s
Copy Event filtered type:%d sender:0x%llx eventInfo:(%@) service filter:%@
Invalid SampleInterval: %@
Powerd has requested active assertions update
Powerd knows about this assertion 0x%0x. let powerd time it out
Failed to create gAssertionsDict
Released connection: %s\n%{public}@
0x%llx: set report interval:%@ client:%@
assertion failure: \"pthread_mutexattr_destroy(&mutexattr)\" -> %llu
IOPMAssertionCreateWithProperties: Call to io_pm_assertion_create failed with kernel error 0x%x
Failed to create dictionary to send message\n
Could not find TCC symbol \"TCCAccessPreflight\"
0x%llx: __IOHIDServiceInit creating queue with high-priority QOS
assertion failure: Unschedule failed queue: %p runLoop: %p
Failed to find %s for create
0x%llx: unschedule from runloop completed
Failed to get PM queue\n
IOHIDConnectionFilterCreate class does not conform to HIDConnectionPlugin protocol
there is a timeout for category %@ and policy %@
createAsyncAssertion: async mode disabled due to SmartPowerNap
Setting async client assertion id to 0x%x
Fail to set parameter with status 0x%x
Unable to serialize matching data
unable to create dictionary
IOPMAssertionCreateWithProperties: pm connection failed
failed to create instance for plugin for %@
Session Filter:%@ filtered copy event (service:0x%llx, type:%d, new type:%d)
Unable to map event queue: (%08x)
Bad arguments
Unable to allocate queue object via _CFRuntimeCreateInstance
assertion failure: IOConnectMapMemory:0x%x
IOHIDServiceFilterFilterSetPropertyForClient %@  %@ -> %@ filter:%@
sendAsyncAssertionMsg failed: powerd xpc connection invalid
assertion failure: \"pthread_cond_init(&session->stateCondition, ((void*)0))\" -> %llu
Successfully opened the IOHIDSession
0x%llx: get report not handled
processCurrentActiveAssertions: No gAssertionConnection
IOPMAssertionCreateWithProperties: One of the arguments is NULL
IORegistryEntrySetCFProperty Failed for kIOHIDActivityUserIdleKey with err : 0x%x
Service plugin %@: %@ never called cancel handler for service: %@
Loading session filter:%@
Received assertion category policies from powerd %@
Setting gAssertionsOffloader timeout to %llu\n
processAssertionTimeout: Turning off assertion idx:%d id:0x%x
restore property %@ to %@
Service:0x%llx  is unregistered, not matching
Invalid ptr=%p size=%d.
0x%llx: IOHIDResource not found
unregisterNotification: invalid ref to 0x%lx
Failed to release assertion 0x%x on timeout
assertion failure: \"!device->cancelHandler && handler\" -> %llu
Connection added: %{public}@
gAsyncModeDisableOverride: enable
__IOHIDEventSystemRelease
Assertion has a category %@
Initial connection to powerd not setup
Failed to load %s
Could not find TCC symbol \"TCCAccessCheckAuditToken\"
IOPMUnregisterNotification: cancelling connection 0x%lx\n
%s: mach_port_deallocate(oldNotify):%s
0x%llx: unresponsive:%@ client:%@
assertion failure: \"!queue->cancelHandler && handler\" -> %llu
assertion failure: \"client->queuePort\" -> %llu
Unable to create event queue via hidd: (%08x)
thread_id=%p
IOHIDEventQueueNotify:%#x
IOHIDServiceFilterCreateWithClass Failed to initialize filter
Failed to create the remoteID to CF for id %@\n
Invalid type
Service filter %@ never called cancel handler for service %@
0x%llx: Packet size is to small for large report, but large report flag is set. reportFlags:%#x entrySize:%u
Failed to get DeviceUsagePairs: %@
%s: HID activity: %d -> %d (service:0x%llx event:%d)
__bootstrap_status:0x%x
Unable to create queue analytics
Assertion 0x%x has already been released
Assertion 0x%x is neither active nor turned off
Failed to create IOPMConnection. rc:0x%x\n
%s: HIDVS ID:%llx iohideventsystem_client_dispatch_virtual_service_notification:%x
No category
__IOHIDServiceLoadObjcServicePlugin plugin did not provide passive matching dictionary %@
__IOHIDServiceCreateObjcServicePlugin Failed to find HIDServicePlugin protocol
0x%llx: Destroy: %@
Failed to find %s for copy multiple, switch to default CFPreferences
assertion failure: Failed to get async event source: 0x%x %p
Unable to open %#x
assertion failure: \"semaphore\" -> %llu
Unable to create analytics description
IOHIDServiceFilterCreateWithClass Failed to find HIDServiceFilter protocol
Failed to register for %s
level_change through kIOPMAssertionLevelKey write.
Failed to create xpc objects to send userActivityRegister message\n
Failed to send IOPMConnection request. rc:0x%x\n
IOHIDEventSystemCreate
Resuming timer
IOPMAssertionCreateWithName: One of the arguments is NULL
Connection: %@ TCC check for service %@: %@ returned right:%llu
io_hideventsystem_queue_start:%#x
No assertion dictionary or logging data to send
Current assertion has been released by powerd gCurrentRemoteAssertion 0x%x gCurrentAssertion 0x%x
IOPMAssertionCreateWithProperties: One of the arguments types is incorrect
IOServiceMatchPropertyTable failed for url %@ for %@
Assertion feature: setting gAsyncMode to %d
No assertions by process
Failed to convert XPC to CF object\n
setAsyncAssertionProperties: Failed to get the assertion details for id:0x%x\n
All actions on enumeration queue completed.
IOHIDEventSystemServiceRemove
Unable to allocate set client reply port attributes
0x%llx: set report not handled
Failed to create xpc msg object\n
Failed to create event system client
no event->parent->eventData
Unable to allocate client reply port
assertion failure: \"pthread_mutex_lock(&(service->queueContext)->lock)\" -> %llu
IOCreatePlugInInterfaceForService:0x%x
level_change->true through kIOPMAssertionTimeoutKey write on an inactive assertion.
Checking getTimeout for string %@
FilterEvent filtered type:%d service:0x%llx eventInfo:(%@) session filter:%@
IOHIDSessionCreate
IOHIDEventSystemAddService
IOHIDSessionClose
Setting category timeout timestamp to %@, monotonic time %llu
invalid io_service_t for %@
io_service_t has no IOCFPlugInTypes for %@
Recreating IOPMConnection id 0x%x\n
HID Session async scheduling initiated.
assertion failure: Schedule failed queue: %p runLoop: %p
Failed to create server dipatch queue
IOHIDSessionFilterCreateWithClass failed for bundle %@
IOHIDSessionUnschedule
0x%llx: IOHIDUserDevice start failed:0x%x properties:%@
Assertion has a policy category timestamp %@
EventToConnection filtered type:%d service:0x%llx connection:%@ session filter:%@
Failed to create XPC message\n
0x%llx: unschedule from dispatch queue completed
bundle invalid for pluginType %@
XPC event: %@\n
PowerD error: 0x%x\n
Received an error in response to copy scheduled wake data\n
_IOHIDCreateBinaryData: %@
%s: %@ is missing the '%s' entitlement
%s: HIDVS ID:%llx create
logAsyncAssertionActivity: unable to find assertion with id 0x%x
assertion failure: Activate failed queue: %p runLoop: %p
Async assertion created with 0x%x, length %ld, %@\n
%s: mach_port_deallocate(notifyPort):%s
%s: HIDVS ID:%llx iohideventsystem_client_dispatch_virtual_service_copy_property:%x
No policies defined for this process
Timeout from category %d
Failed to create xpc reply object
IOHIDConnectionFilterCreate Failed to initialize plugin
Connection: %@ denied match of service %@: TCC %@ right:%llu
Unable to serialize event
IOHIDSessionCreate failed to find symbol %@ for bundle %@
%s: HIDVS ID:%llx iohideventsystem_output_event_to_virtual_service:%x
Async assertion: setting offload delay to %llu
IOHIDEventCreateDigitizerEvent event is null
Service added: %{public}@
0x%llx: kIOHIDResourceDeviceUserClientMethodPostReportResponse:%x
failed to get interface for plugin for %@
event system =\n%s
Sending initial message to powerd for async assertions
IOHIDService compatibility thread running at priority %d and schedule %d.
%s: Event enqueue dropped:%d consecutive events
%s: iohideventsystem_client_dispatch_service_removal:0x%x
processAssertionTimeout: Removing idx:%d id:0x%x
start failed (%s) for plugin for %@
Category %@ not found
No plist for plugin url %@ for %@
IOHIDEventSystemCreate error
Can not locate kernel service
Failed to register for reconnect with powerd 0x%x
0x%llx: Failed to open service
Invalid reply type\n
Received connection invalid error for connection 0x%lx. UnregisterNotification
Failed to create event at index=%d , eventDataMaxSize: %u < eventDataSize: %u
IOHIDEventSystemOpen:%lldus
QueryInterface:%x
Unexpected data type in gAssertionsDict for id:0x%x\n
Could not find TCC symbol \"TCCAccessRequest\"
Event handler is called %@\n
assertion failure: \"pthread_mutex_unlock(&(queueContext)->lock)\" -> %llu
%s: mach_port_request_notification(MACH_PORT_NULL):%s
Bad matching dict
%s: HID activity: start reporting with interval: %ds
processAssertionUpdateActivity unread-count %d
IOConnectGetService Failed with err : 0x%x
Failed to create xpc connection
assertion failure: Invalid dispatch state: 0x%x
IOHIDEventServerCreate
0x%llx _IOHIDServiceCreate failed to load service plugin ret: 0x%x score: %d objcScore: %d
assertion failure: \"pthread_mutex_init(&session->queueContext->lock, &mutexattr)\" -> %llu
processAssertionTimeout: Removing from gActiveAssertionsDict: 0x%x
Failed to create connection\n
Fail to get parameter with status 0x%x
Set cursor bounds failed:0x%x
%s: HIDVS ID:%llx iohideventsystem_copy_matching_event_from_virtual_service:%x
handleAssertionLevel for 0x%x to %d: %@
IOHIDEventSystem TCC matching: could not load Security.framework, gating disabled
Failed to create dictionary to send message
io_service_t has no plugin for %@
0x%llx: IOHIDService property %s incorrect type: %@
IOHIDServiceFilterCreateWithClass class does not conform to HIDServiceFilter protocol
%s: HIDVS ID:%llx Invalid parameters: key:%@
fetchAssertionCategoryPolicies: Reply is not a dict
Failed to create ASBM services\n
Re-syncing assertions
assertion failure: Failed to create notification port %p
io_hideventsystem_do_client_refresh:0x%x
assertion failure: \"pthread_mutex_lock(&(queueContext)->lock)\" -> %llu
0x%llx: IOHIDServiceSetElementValue time:%lluns
unable to make mach memory entry. (%08x)
0x%llx: __IOHIDUserDeviceStartDevice:0x%x
Shipping charge limit data not found\n
Assertion index 0x%x already exists
Received active assertions from powerd %@
__IOHIDEventSystemCreateNotification
0x%llx: Set report interval current:%d new:%d result:%d events:%@
%s: Unable create activity notification
%s: HIDVS ID:%llx: iohideventsystem_client_dispatch_virtual_service_set_property:%x
processAssertionTimeout: Not found in gActiveAssertionsDict: 0x%x
IOHIDSessionFilterCreateWithClass class does not conform to SessionFilter protocol
assertion failure: \"queuePort\" -> %llu
Add session filter:%@
handleAssertionLevel: unable to find assertion with id 0x%x
Set fixed mouse location failed:0x%x
Enabled flag not found\n
assertion failure: \"retainCount < (2147483647 *2U +1U)\" -> %llu
Entry of IOHIDService property %s incorrect type: %@
%s: HID activity: stop reporting
QueryInterface(kIOHIDDeviceDeviceInterfaceID):0x%x
assertion failure: Failed to get queue port %p %p
Client must be scheduled with dispatch queue or runloop
Unable to get serviceID for IOHIDServiceClient: %@
Failed to find %s for copy, switch to default CFPreferences
assertion failure: \"!manager->runLoop && !manager->dispatchQueue\" -> %llu
SecTaskCreateWithAuditToken failed for pid:%d
%s: Unable to create activity timer
%s: Sent client refresh msg, status:%#x
Async sssertion bufffer initialized.
Failed to get UUID. rc=%d\n
io_hideventsystem_remove_virtual_service:%x
posting reset to (%p)(%p, %p)
setAsyncAssertionProperties for 0x%x %@:%@
_releaseAsyncAssertion: Failed to get the assertion details for id:0x%x\n
assertion failure: \"client->notifyPort\" -> %llu
0x%llx: IOHIDServiceRequestTerminate
gAsyncModeDisableOverride: disable
[%#llx] Invalid kIOHIDTCCServiceKey property, expected String
Connection removed: %{public}@
IORegistryEntryIDMatching:NULL
handleAssertionTurnOff: Released assertion id 0x%x
assertion failure: \"__IOHIDQueueSetupAsyncSupport(queue)\" -> %llu
insufficient buffer data available, size: %ld, length: %ld
IOServiceGetMatchingServices:0x%x
[%s] Process has entitlement %s on Non-Internal build
Set cursor enable failed:0x%x
IOHIDSessionRelease
assertion failure: \"pthread_mutex_unlock(&(session->queueContext)->lock)\" -> %llu
Sending Assertion release message for assertion Id 0x%x\n
Failed to create event at index=%d , eventDataSize: %u < minimum size: %u for type: %u
HID Event System Client refreshed but no services returned
HID Session async root queue running at priority %d and schedule %d.
%s: mach_port_allocate(sendPossiblePort):%s
powerd released our connection
0x%llx: os_workgroup_interval_start error: %d, service %@
Client record is not serializable for %@
Unexpected message from async assertions connections\n
xpc_user_sessions_get_foreground_uid failed: %d - %s
assertion failure: \"pthread_mutexattr_init(&mutexattr)\" -> %llu
No timeout ts. Remove from timed list
Unable to create event attachment storage
Unable to retain service: 0x%x
%s: Connection filter added:%@
Failed to send mach port for IOPMConnection id 0x%x. rc:0x%x\n
__IOHIDServiceCreateObjcServicePlugin Failed to initialize plugin
IOHIDSessionOpen
plist invalid for pluginType %@
CreateSessionFilterClass
Category %@ has a policy %@
IOPMAssertionCreateWithProperties: Failure copying assertion properties. Collect backtrace %llu
Failed to find %s for set domain, switch to default CFPreferences
io_service_t has invalid IOCFPlugInTypes for %@
XPC event handler: %@\n
Received an error in response to copy '%s' data\n
IOHIDSession close completed
CopyServiceRecords deep copy failed. Service record for %@ is not serializable.
IOHIDConnectionFilterCreate Failed to find HIDConnectionPlugin protocol
0x%llx: Start: %@
powerd returned assertion id 0x%x for async id 0x%x \n
assertion failure: \"!manager->cancelHandler && handler\" -> %llu
Failed to create event at index=%d eventCount=%d eventDataOffset=%d lenght=%ld
HID Session async scheduling complete.
__IOMIGMachPortRelease mach_port_mod_refs:%s
IOHIDConnectionFilterCreate failed to find symbol %@ for bundle %@
IOHIDEventSystemRelease
%s: mach_port_request_notification(notify):%s
%s: mach_port_request_notification(notify) unexpected old notify port %#x
IOHIDEventSystemClose
Bad matching event
IOHIDEventServerUnschedule
Failed to create gAssertionConnection\n
Irrecoverable error for assertion creation\n
probe failed for plugin for %@
Failed to find %s for set multiple , switch to default CFPreferences
Set on screen cursor bounds px:%d py:%d minx:%d miny:%d maxx:%d maxy:%d
%s: mach_msg(sendPossiblePort):%s
Suspending timer
assertion failure: Cancel failed queue: %p runLoop: %p
Service removed: %{public}@ %@
__IOHIDServiceLoadServiceFilterBundles failed to find symbol %@ for bundle %@
Registering for assertion policy changes
powerd returned err 0x%x to create assertion %@. Dropping the assertion\n
Failed to find %s for synchronize, switch to default CFPreferences
IOServiceAddInterestNotification: 0x%x
_IOHIDCreateBinaryData fail
io_hideventsystem_dispatch_event_for_virtual_service:%x
Loading symbol for principal class:%@ from bundle
0x%llx: kIOHIDResourceDeviceUserClientMethodHandleReport:%x
Event filtered type:%d sender:0x%llx eventInfo:(%@) service filter:%@
%s: mach_port_deallocate(unusedNotify):%s
Set on screen cursor bounds failed:0x%x
Failed to create XPC connection to PowerD\n
Unable to create IOHIDEvent with length:%d
Received processCheckAssertionMsg with active assertion 0x%x
Received a release not for gCurrentRemoteAssertion:0x%x. Received 0x%x
bootstrap_look_up2 failed: %s
Assertion retain not supported in async mode\n
Could not load TCC
API will be deprecated soon.  Please use IOHIDEventSystemClientCreate.
0x%llx: os_workgroup_interval_finish error: %d, service %@
__IOHIDServiceCreateObjcServicePlugin class does not conform to HIDServicePlugin protocol
Removing 0x%x from TimedList
onePlugin invalid for pluginType %@
Virtual service (id: %llx) does not exist
%s
IOHIDEventSystem TCC matching: tcc_authorization_check_audit_token unavailable, gating disabled
HID Event System Client refreshed with %ld services, cached matching had %ld services
CFPlugInFindFactoriesForPlugInTypeInPlugIn failed for plugin url %@ for %@
IOHIDSessionFilterCreateWithClass Failed to find HIDSessionFilter protocol
Releasing assertion locally id 0x%x
No current assertion. Sending all activity till now
IOHIDEventSystemOpen
All actions on server queue completed.
%s: Server died, preventing any future MIG calls
IOPMAssertionCreateWithProperties: io_pm_assertion_create failed with error 0x%x
Unknown client type: %d pid:%d
invalid matching dictionary: %@
IOHIDSessionSchedule
0x%llx: Unable to create analytics description
%s: Event enqueue error:0x%08x type:%d sender:0x%llx
Checking for timeout for category %@ %d
Failed to create xpc reply object\n
0x%llx: set batch interval:%@ client:%@
Assertion 0x%x not found to activate
0x%llx: os_workgroup_interval_finish(cancel) error: %d, service %@
[%#llx] Invalid entitlements property, expected Array or String
Setting assertion timeout to fire in %d msecs for timeout_ts %llu
IOHIDEventSystemAddServices
HIDVS (id:%llx) client does not exist
Insufficient permissions to set kIOHIDSessionCASecureLayerOnScreenKey for UUID: %@
%s: Filtered event type:%@ sender:%#llx eventInfo:(%@) -> outEventInfo: (%@)
assertion failure: \"completionElement\" -> %llu
IOHIDSessionFiltersClose
Creating deep copy of record belonging to service: %@
0x%llx: Unable to create queue analytics
No connection to powerd
Turning off assertion 0x%x: %@
Unable to allocate acquire client reply port attributes
Failed to create useractiveRefs
IOHIDEventSystem TCC matching: SecTask code sign status SPI unavailable, gating disabled
Invalid BatchInterval: %@
Loaded %ld HID plugins (%@) %@
called with a NULL callback
IOHIDEventSystemOpen error
Set cursor enable:%s
HIDVS (id:%llx) invalid property key
Service: %@ cancellation timer timed out
SetProperty called %@=%@ caller=%@
IOHIDSessionRegisterFilters
%s: HIDVS ID:%llx _iohideventsystem_copy_event_from_virtual_service:%x
No timeout for category %@ for policy %@
No AssertionActivity in xpc reply
IOHIDEventSystemCreate:%lldus
offloadAssertions called with gCurrentRemoteAssertion 0x%x
Replying to assertion check message with count %d token:%llu\n
assertion failure: \"pthread_mutex_unlock(&(service->queueContext)->lock)\" -> %llu
sendAsyncAssertionMsg failed: powerd xpc connection interrupted
processAssertionUpdateActivity: No gAssertionConnection
pluginPath == NULL, unable to allocate a CFString
Failed to create CF properties: 0x%x\n
0x%llx: IOServiceAddInterestNotification 0x%x
Update assertion policy %llu
CFPlugInCreate failed for url %@ for %@
0x%-16llx 0x%-16llx 0x%-16llx 0x%-16llx 0x%-16llx
Add filter:%@ for service:0x%llx
%@ is not serializable
Missing state in reply\n
Failed to create PM queue\n
HIDVS (id:%llx) does not exist
handleAssertionTimeout: Setting assertion timeout to fire in %llu secs
no factories for plugin for %@, kr = 0x%x, factories = %p, factoryCount = %ld
IOHIDEventSystem - service queue termination
io_hideventsystem_set_properties:0x%08x result:%d
CFDictionaryCreateMutableCopy fail
%s: iohideventsystem_client_dispatch_notification_results:0x%x
Failed to convert CF dictionary to xpc object\n
Failed to create XPC connection\n
Created IOPMConnection with id 0x%x\n
Failed to create message\n
Invalid ReportInterval: %@
Timeout is less than 0 %d
handleAssertionTimeout fired %llu
Timeout: assertion id 0x%x with time %llu, policy timeout %llu
Received an error in response to IOPMCopyActiveAsyncAssertionsByProcess
Setting Assertion State for PID %d to %d\n
Failed to find %s for copy domain, switch to default CFPreferences
Wake progress from %d. data: 0x%x\n
Failed to register for reconnecting with powerd. rc:0x%x
bootstrap_look_up_per_user failed: %s
IOHIDServiceFilterCreateWithClass failed for bundle %@
Malformed PropertyMerge value in bundle: %@
IOHIDServiceFilter cancel handler invoked more than once for filter:%@
Sending assertion create msg for id 0x%x:%@\n
CreateSessionFilter
Session Filter:%@ filtered copy event (service:0x%llx, type:%d)
0x%llx: IOServiceOpen:0x%x
Received an error in response to copy assertion activity
Connection: %@ not entitled to match protected service: %@
IOHIDSessionUnregisterServices
%s: mach_port_deallocate(reply_port):%s
Error: the client with pid %d is missing the '%s' entitlement.
offloadAssertions fired
Missing key '%s'\n
0x%llx: set property:%@ value:%@ client:%@
0x%llx: Set batch interval current:%d new:%d result:%d
%s: Unable to create DISPATCH_SOURCE_TYPE_MACH_SEND for reply port
Failed to create event at index=%d , eventDataSize: %u < sizeof(IOHIDEventData): %lu
IOHIDEventSystemServer died. Reestablishing connection.
Failed to register for server availability: %d
IOHIDSessionCreate - Load bundles
Logging all %ld activity to powerd\n
mach_port_deallocate(bootstrap_port) %s
IOHIDSessionFilterCreateWithClass Failed to initialize filter
Failed to update machport for IOPMConnection id 0x%x. rc:0x%x\n
Kext %s-space log filter changed from 0x%x to 0x%x.
IOUSBDeviceDescription: pid/vid/ver=%04x/%04x/%d class/sub/prot=%d/%d/%d Mfg:%@ Prod:%@ Ser:%@\n%@
Established
HIDCapsLockLED
Safe Boot
VAC-T
UPSShutdownAtLevel
com.apple.iokit.iomigmachport
ElementType
v12@?0i8
UTF16 Big Endian
 dependencies
%s is not valid.
Started %s.
TimeoutActionTurnOff
Audio Stream Data:\n
(missing)
Can't stat source folders for cache file %@.
%s added %u-byte %scompressed executable to mkext.
AppleSmartBattery
setHIDEventService:
Requesting unload of %s%s.
%s (version %s%s%s): same version, different UUID (%s) is loaded.
%s is not valid; omitting from mkext.
SensorPropertySupported
Position 
PrimaryUsagePage:
Total Channels: %d Active Channels: %d\n
DolbyVision LL YCbCr 4:2:2 (HDMI tunneling)
NO
%-20.20s %llu us\n
LatencyServiceOpen
Bad mkext magic/signature.
ID
%lld 
BT.2020 (RGB)
HIDPreferencesSetMultipleForInstance
HIDClickSpace
batteryCycleCountData
CFBundleIdentifierKernel
/usr/appleinternal/lib/HIDPlugins
IONotificationPortSetImportanceReceiver
dominoMainDisplay
!hid_pthread_attr_init(&attribute, kIOHIDInterruptThreadPriority, kIOHIDInterruptThreadPolicy)
com.apple.private.hid.client.motion-event-privileged.internal
adapterDetails
%s, version %s recorded at index %d in the identifier lookup dictionary.
OneBitAudio
IOHIDEvent
setPowerSourceDetails returned 0x%x\n
Start
Nameless (via IOPMAssertionCreate)
d
OSBundleRequired
sizeof(IOCircularDataQueueDescription) == inband_outputCnt
filterEvent:forService:
com.apple.powermanagement.sleepservices
IOHIDDeviceDispatchMach
%s %d - cannot allocate memory for target string
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n
External
PrimaryUsage
Reading list of all kexts requested by kernel since startup.
YCbCr 4:2:2 (HDMI tunneling)
AVI
key
}\n
Unicode
DeviceUsage
OSKernelResource
Dolby TrueHD (MAT1.0)
HIDMouseAcceleration
IOKit IOGetSystemLoadAdvisoryDetailed
queueHeaderShadow->allocMemSize == map_size
%-20.20s\n
Direction Pad Left:
ServiceEntitlements
DeviceUsagePage:
UPS Power
now
IsPromoted
configurations
Internal error converting URL
Flushing dependencies for %s.
Front Right Wide
scheduledby
AppleUSBXHCI
/IOKit/PowerManagement/SystemLoad/Detailed
non
assertionActivityUpdateData
/usr/appleinternal/lib/HIDPlugins/SessionFilters
Front Left
File not found
unknown CPU architecture
type
com.apple.system.powermanagement.useractivity2
SCPreferencesCreate
HandFlick
OSBundlePrelinked
Quality:
%s (version %s%s%s) is loaded.
state.dictionaryIDRefDictionary
Console
deviceID
Standard
Closed
%s not in base path %s for identifier->path cache - marking.
Mkext plist compressed size is %u.
xvYCC601
HIDCapsLockLEDOn
PowerSource
not serializable
BatteryPacks
com.apple.
SCPreferencesSetValue
%-20.20s %@\n
Kexts with a kernel library < v6.0 must set MODULE_VERSION the same as CFBundleVersion to load on kernel < v6.0.
MobileMotionModule
setCancelHandler:
Cache file %@ - owner not root; not using.
%s: %lld.%0*lld\n
SetPower
LinearPCM
Dolby Atmos (MAT2.1)
Hand
OBJC_CLASS_$_%@
 off
Can't create kext: missing or non-string path in identifier cache entry %d.
HDCP
<%s %s>
 %@=%d
com.apple.kernel.unsupported
TimeoutActionRelease
kern.waketime
4:3
MPEG
integer
IODeviceTree:
Proximity
AsyncClientAssertionId
<%s ID=\"%d\">
DeviceUsagePage
com.apple.private.hid.client.admin.internal
Video Color
%02x%s
1.2.12
deviceSubClass
Dolby TrueHD (MAT2.0)
HIDPreferencesSynchronizeForInstance
PowerRelativeToShutdown
EventFilterMask
</key>
powerInfoPrecise
push 
Extra Button R4:
Info dictionary property value is of incorrect type
Kext identifier->path cache for %s - version %d unsupported.
Cache file %@ - wrong permissions (%#o, should be %#o); not using.
Failed to read contents of %s, CFURL error %d.
PresentActive
IOGeneralInterest
LoginWindowProgress
IOHIDUserDevice
NextThreshold:
mkext data
ReprotectLink
</%s>
IODPHDMIControllerPort
Embedded
HIDServiceAccessEntitlement
Queue
Validation Failures
Error communicating with kernel - %s.
 not
com.apple.iokit.statenotification.set
IOUSBHostDevice
TargetBrightness:
Transport:
GlobalUniqueID
Link Mode:    %s\n
USBDeviceCommand
Intermediate
lastNotifyTime
%-20.20s True\n
Supported Features
IOHIDValue
Face Button A:
Location:
LatencyCopyProperty
%s - dependencies already resolved.
Symlink points outside of bundle.
HIDAnalyticsEventCancel
IOService
IOHIDUserDevice State
%s:%u: %s(): %s
DisplayDims
SCPreferencesGetValue
Source
state.data
com.apple.system.powermanagement.prefschange
Successfully stopped %s.
Kext Request Info Keys
/System/Library/HIDPlugins/ServicePlugins
4:5
HighPowerMode
Unsupported
0 Gbps (FRL disabled)
ActivityTimeout
AngleDegrees:
3:4
b
Personality CFBundleIdentifier names a kext that is not loadable (run kextutil(8) on it with -nt for more information)
OS
y
Found plugin %s.
SleepWakeUUID
%-20.20s %08x\n
IONetworkInterface
IOResources
IOUSBDeviceData
TimedOut
Off
array
SCError
HIDKeyboardModifierMappingSrc
Mkext plist has no kexts.
%s: %s\n
Audio Channel Layout
HIDParameters
Can't load %s - ineligible during safe boot.
com.apple.iokit.IOServiceAuthorizeAgent
failed to open io_service_t err=0x%x
CH2:
YCbCr 4:2:2
TPS4
DeepSleep
com.apple.system.accpowersources.source
HIDObjectUUID
getBatteryHealthState
Stage:
DriverKit
MotionGesture
Direction Pad Down:
Multiple kexts for these libraries occur in the dependency graph
timeout
SessionFilterDebug
.kext/
Statting %s for suffix.
%s does not declare a kernel dependency; using %s.
HIDPointerAccelerationType
DST
devices
UTF16 Little Endian
PerformanceWarning
MaxChannelCount
RestartInterfaces
options
IOHIDEventSystemClientDispatchMach
Libraries declared for both com.apple.kernel and a com.apple.kernel.* component.
Kexts may not link against com.apple.kernel; use either com.apple.kpi.* libraries (recommended), or com.apple.kernel.* (for compatiblity with older releases).
unexpected end of buffer
DarkWake
notificationCount
/AppleInternal/Library/HIDPlugins/ServicePlugins
HIDAnalyticsEventAddField
state.setIDRefDictionary
0x%lx
com.apple.iokit.cfplugin
AuxiliaryPressure:
com.apple.kpi.unsupported
Protection Command
Limited
com.apple.system.accpowersources.attach
CoreDisplayProgress
/System/Library/HIDPlugins
PortVariant
TrainLink
no
Kexts found for these libraries lack valid OSBundleCompatibleVersion
TPS1
SCPreferencesCreateWithAuthorization
Ry:
Transition: Enter
matchConnection:
com.apple.kpi.
EventTime
CFBundleIdentifier
    
com.apple.powerd.assertionoffloadtimer
VGA
builtin-battery
IOAccessoryIDBusBulkData
ReleasedThreshold:
<data>
EventFilterTimeoutCount
/Library/Apple/System/Library/HIDPlugins/ServiceFilters
UnsafeColorElementIDs
Transport Type
UsagePage:
 for:
Internal error, invalid argument to __OSKextCheckURL.
OSBundleCPUType
com.apple.private.hid.client.service-protected.internal
MaxPropertyGetTime
Kext Request Lookup Address
should be %s
HIDPreferencesSetForInstance
IOHIDManager
Total Latency:
/System/Library/Frameworks/Security.framework/Security
KextIdentifiers
com.apple.private.hid.client.event-monitor.internal
SleepServiceImmediate
%u
%-20.20s 0x%08x\n
Kext isn't loadable during safe boot.
Temp cache file name too long: %s.
Cache file %@ - group not wheel; not using.
Start Matching Exclude Level
Can't get info dictionary for %s.
IOSleepSupported
Driver Extension lacks appropriate value for OSBundleRequired, and will not be launched without kextd present. Use one of 'DriverKit' or 'Safe Boot.'
OSBundleUsesAbsolutePath
w
Created
Failed to get %s for portType=%d, portNumber=%d, portVariant=%d\n
Hibernation
HIDNumLockState
velocityDegreesPerSecond:
__OSKextCreateKextsFromURL
ClientSuspend
Color Attributes:\n
CalibrationMax
Power
OSBundleUUID
Found %s.
Front Right Center
!parent
%@%@
eventtype
Temperature
Shake
UNKNOWN
NormalizedForce:
DEXT
ICH8 ATA/100
client
Touch 
EventTypeCounts
com.apple.hid.analytics.service.dispatchEvent
%s failed to compress executable.
OSBundleAllowUserLoad
uniqueDeviceID
SLCheckIn
*
Can't unserialize kext request response: %s
HIDAnalyticsEventSetIntegerValueForField
Stylus
%-20.20s %dx\n
Can't create kext: missing or non-string bundle package type in identifier cache entry %d.
s
IOPMPowerSource
Dependencies have validation problems
BT.2020 (YCbCr)
IOBatteryInfo
LowPowerMode
category < kIOHIDLogCategoryCount
Can't read info dictionary for %s: %s.
ActivityState
Protection Command (with source and AUP data)
Video
WakeOnMagicPacket
Flushing info dictionary for %s.
%@ - %@
com.apple.private.hid.client.debug-tool
Rear Right Center
object
IOHIDDevice
OSKEXT_BUILD_DATE 16:20:56 Oct  3 2026
com.apple.kernel.
Executable kext %s with no dependencies?!
ResourcesUsed
SleepDisabled
CurrentState
Kext identifier->cache for %s - cache version missing/invalid.
Indirect dependencies can't be resolved
IsCoalesced
IOHIDEventQueue
Memory allocation failure.
Channel %d: %s\n
DefaultDeviceDescription
BT.2020 (YcCbcCrc)
TCCAccessCheckAuditToken
__IOHIDEventSystemRegister
Built-In
IOMIGMachPort
IOHIDServiceFilter uuid:%@ name:%@ %@
Auto
Dolby TrueHD (MAT2.1)
Low Frequency Effects
tcc_authorization_check_audit_token
%s Element\n
Mask:
LatencyCopyEvent
ClientRecords
Capture
Can't determine actual safe boot mode - sysctl() failed for KERN_SAFEBOOT - %s.
Opening %s for map.
OSBundleLoadAddress
Interfaces
xvYCC709
AC Power
com.apple.system.accpowersources.timeremaining
Unload
GTF
HIDPreferencesCopyForInstance
No Description
IONetworkInterfaceProperties
Azimuth:
ServiceRecords
Shoulder Button R1:
TimeoutAction
%s: 
hideventsystemclient.default.queue
Invalid cache format %d specified.
PresentPassive
Thumbstick Button Right:
OSBundleDebugLevel
memory exhausted
HIDPreferencesSynchronize
<%s ID=\"%d\" %s>
IOAppPowerStateInterest
_kTCCAccessRequestOptionSyncCallback
f
systemAssertionTimeout
FromEdgeTip 
com.apple.iokit.powerdxpc
ServicePluginDebug
Executable does not contain code for architecture
Personality matches on IOResources but IOMatchCategory is missing or not equal to its IOClass; driver may be blocked from matching or may block others
dis
Error initializing zlib uncompression for %s.
%s (version %s): is%s started.
IOMatchCategory
forward reference detected
RequestTerminate
<!-- 🤦 -->
[^/]+
%-20.20s 0x%x\n
Can't create kext cache under %s - group not wheel.
Reading requests from kernel.
Released
%x, %lx, 0x%llx, 0x%llx\n
state.stringIDRefDictionary
a
Velocity
_kasan
AssertName
MaxLaneCount
Front Right High
initWithConnection:
Layout:\n
IOHIDSessionFilterRef uuid:%@ name:%@ %@
Name
Pointer
LongSqueeze
Phase
Can't stat %s - %s.
Compressed write error for cache file %s - %s.
mkext URL = \"%@\", 
Authenticating %s file/directory %s.
SetDeviceDescription
Statting %s for map.
Local-Root
com.apple.private.hid.client.event-dispatch
claimSystemWakeEvent
SCDynamicStoreSetNotificationKeys
StandardType:
DeviceUsagePairs:
Link Command (with source)
OSBundlePath
com.apple.kext.load
FrameworkBundleID
ColorModes
Serial
chargeSocLimitAction
Rate:
StartLink
BatchInterval
IOPower:/IOPowerConnection/IOPMrootDomain
DestroyFVKeyOnStandby
%-20.20s %u\n
LatencyDispatchEvent
Failed to remove temp cache file %s - %s.
%s - loaded dependency %s lacks valid OSBundleCompatibleVersion.
Load
v12@?0C8
Begin
IOHIDEventSystemClient.c
Couldn't read resource URL in %s for resource %s.
Sender
/System/Library/PrivateFrameworks/TCC.framework/TCC
aud 
 validation
USBDeviceCommandParameter
PrioritizeNetworkReachabilityOverSleep
uuid
MaxPropertyNotificationHandlingTime
VESA
MotionActivity
Orientation type:
9:14
9 Gbps (3Gbps/lane * 3 lanes)
Inhibit
SCDynamicStoreCreate
'%@' -> '%@'
IODPDevice
IOAVService
NXSystemInfo
Properties
Can't read kernel CPU info from IORegistry (absent or wrong type).
ProximityWake
IOPacketFilters
IOHIDEventSystem.c
IdleNotificationTime
Add Child
EstimatedAltitude 
rh:
NaN
Can't create kext from cache: %s is already open and has a different CFBundlePackageType from identifier->path cache entry %d.
(executable from mkext)
Can't create kernel load request for %s.
KeyboardLanguage
assertionProperties
IOCFPlugInTypes
Dispatch Latency:
Cancelled
Can't determine real path for %s (%s)
DarkWakeBackgroundTasks
SymbolicHotKey
TransducerIndex:
Can't create kext: invalid CFBundleVersion in identifier cache entry entry %d.
 failed
assertionActivityUpdateOverflow
HIDAnalyticsEventAddHistogramField
set
__LINKEDIT
propertyCacheMiss
dext
Loaded kext info from kernel is wrong type.
Orientation
%s: internal overrun (%p, string_index: %d, file_end: %p) in executable file (%s).
AssertStartWhen
Score
DCI-P3 (Theater)
VendorDefined
HIDServiceSupport
setting load address of %s to 0x%0llx
PSR:           %s\n
AdobeYCC601
false
SLCheckInCapability
NextEventTimeStampDelta
Startup
Finished reading cache file %s.
%@:
Set Power
ServiceFilterDebug
Warnings
HIDInterfaceID
identity
unknown
%-20.20s 0x%016llX NON KERNEL SENDER\n
buttonState: %ld
Gyro
DSC:          NO\n
Unprotected
Dynamic Range & Mastering
IOService:/
%@%@/%@
DoubleSqueeze
IOParentMatch
com.apple.powermanagement.assertionexception
IOHIDActivityUserIdle
copyEvent:matching:options:
Kernel error handling kext request - %s.
Vendor Specific Data Block
<%s IDREF=\"%d\"/>
HIDKind
com.apple.private.hid.client.event-filter
ActivityTime
StreamSampleRate
Front Left Wide
GameController
Usage:
Reading resource %s.
Failed to remove personalities of %s from IOCatalogue - %s.
Downstream
DesktopMode
%@#%@#%@#%@#%@
openOptions
IOHIDResource
Close
com.apple.system.powersources.percent
IOUserEthernetResource
ups
Can't get executable for %s (architecture %s).
Major
IOKit.framework:IONotificationPortGetRunLoopSource bad CFMachPort, %s\n
Can't stat path %s - %s.
NameChange
IOAVDevice
 = 
Digitizer
Type:
Delay Autounload
Kext contains symlink at %s which points outside of its bundle at %s; rejecting.
%-20.20s ERROR\n
SleepFailure
FullWake
onenessState
Hot Plug
 %@=%@
IOHIDEventSystemClientIsUnresponsive
eventMatching:forClient:
Loading %s.
HDCP2
SwipePending 
%s is already open; returning existing object.
Open failed for %s - %s.
AsyncRemoteAssertionId
Front Center
DoCFSerialize
description
Rotation
ValueType:
Joystick Axis Y:
Dependencies aren't loadable during safe boot
MinLaneCount
EnergyMode
OSKernelCPUType
Stop
sRGB
HIDWaitCursorFrameInterval
HIDSubinterfaceID
Date of first use
Button
NormalizedPositionY:
ClickDownPredicted 
Left Headphone
IOProbeScore
assertionCheck
Flags:
Sequence:
Open
version
MIPI
%@#%@
IODeviceTree
Face Button X:
Requesting start of %s.
, DSC (%f bpp, passthrough)
RestartAfterKernelPanic
AttributeData:
ChildEvents:
yes
IOKitPersonalities
OSKernelCPUSubtype
Can't create %s - %s.
disk 
IOHIDServiceConnectionCache
IOHIDManagerStateQueue
DockSwipe
Validating %s.
TPS2
IOCircularDataQueueCreateWithConnection
Kext library architecture is %s (unchanged).
%s found link dependency %s.
Sleep On Power Button
AppleSmartBatteryManager
Compressed executable from %u to %u bytes (%.2f%%).
PressedThreshold:
OSKextIdentifierCacheVersion
Progress
MayBegin
kernel
UPSDefaultThresholds
%-20.20s %s (%d)\n
com.apple.kpi.private
Audio Channel Layout Data:\n\n
Rejecting invalid/inauthentic kext for bundle id %@ at location %@.
assertionUpdateActivity
com.apple.system.powersources.source
isOpen
TCCService
Failed to serialize kext request.
Traditional gamma (HDR)
%s - no compatible dependency found for %s.
Product
SubType:
<string>
assertionTimeout
State:
Cancel 
HardwareAddress
_%s
Couldn't read resource file %s.
Rear Right
Personality
batteryChargingIconoGraphyAction
SerialNumber
v16@?0r^v8
***UNKOWN***
v24@?0Q8Q16
CalibrationDeadZoneMin
Kext was not created from an URL and can't be authenticated
%s already has dependencies resolved.
Mkext checksum error.
com.apple.private.hid.client.event-monitor
PreventUserIdleSystemSleep
DSC:          YES (%f bpp, passthrough)\n
batteryChargingIconoGraphy
ServiceRecord
PrepareLink
GestureType:
ServiceID
IOHIDService - RunLoopCompatibilityThread
unknown error
activityStateChangeCount
com.apple.private.hid.client.motion-event-privileged
AbsentWithDisplay
en
Can't load %s - dependency authentication problems.
batteryShippingChargeLimitState
chargeSocLimitToken
Undefined
Tap Count:
Length
Kext has a CFBundleExecutable property but the executable can't be found
CreatorBacktrace
DisplayIntegrated
%s
EventType:
Unit
userDeviceQueue
CFBundlePackageType is DEXT and bundle declares CFBundleExecutable; use only one.
False
MPEG2
Dolby Atmos (EAC3)
Front Right
<IOHIDNotificationRef %p (ref:%d xref:%d), flags:%x  %p,%p,%p,%p,%p,%p>
URL = \"%@\", 
Direction Pad Right:
HIDPreferencesCopyMultipleForInstance
dict
Extra Button L4:
Kexts with a kernel library < v6.0 must set MODULE_NAME the same as CFBundleIdentifier to load on kernel < v6.0.
Error encountered, unmapping executable file %s (offset %lu, %lu bytes).
assertionActivityUpdateProcessList
IOPMSleepFailure
SCPreferencesApplyChanges
LowSNRSwipe 
Personality has no CFBundleIdentifier; the kext's identifier will be inserted when sending to the IOCatalogue
Directories
com.apple.kpi.dsep
UTF32 Big Endian
LocationID
Kext personality %s subentry is not a dictionary
Process must be running as root to load kexts.
%s.%06d
VersionNumber
A system kext has a property set that it shouldn't
Description
Altitude:
???
com.apple.kernel.6.0
Hibernate Mode
IOHIDQueueDispatchMach
OSKextIdentifierCacheKextInfo
Can't read loaded kext info - current architecture %s != kernel's architecture %s.
Failed to create kext request.
AdobeRGB
Overscan
data
assertion failure: Device already scheduled
HIDConnectionPlugin
Rate Controlled
HIDServicePlugin
%s found %s%s%sdependency %s for %s%s.
%s\n
zlib inflate failed: %s.
Can't create kext: path in identifier cache entry %d doesn't name a kext.
StandardType
GRGB Tunneled as YCbCr422 (Even line red)
Creating %s.
BatchInterval:
Audio Link Data:\n
manufacturerString
On
IOCFSerialize.c
-----------------------------------------------------------------------\n
user
%F %H:%M:%S
IOHIDTransaction
LongPress
File access failure; can't open, or I/O error
Architecture %s not found by CPU info (type %d, subtype %d), trying by name.
HIDAnalyticsEventActivate
D10.2
Accuracy:
Administrative
%s - dependency for %s lacks valid OSBundleCompatibleVersion.
TimeoutSeconds
BT.709
PackID
IOHIDEventSystemClient
ID = \"%@\"
BuiltIn:
assertion failure: Get report block already set
Releasing CFBundle for %s
com.apple.kpi.kcov
/System/Library/HIDPlugins/SessionFilters
UnprotectLink
v8@?0
Dynamic Power Step
Transition: Exit
AppleClamshellState
Manufacturer
Squeeze
%s:%@
Kext Request Result Code
leeway
NotificationActive
HIDRMHash
ZoomToggle
%s: internal overrun in executable file (%s).
filterSetProperty:forKey:forClient:
IOUserClass
%08x: 
/System/Library/PrivateFrameworks/HIDPreferences.framework/HIDPreferences
<
HIDResetKeyboard
CalibrationMin
SwipeRight 
MaxEventLatency
GPUSwitch
Can't create kext from cache: %s is already open and has a different CFBundleIdentifier from identifier->path cache entry %d.
Flushing load info for %s (%s dependencies)
assertionActivityLog
Kext declares no kernel/KPI libraries; if it references any kernel symbols, it may fail to link.
Reading load info for all kexts.
DMT
%@#%04lx#%04lx#%016lx#%ld
cursor
File owner/permissions are incorrect (must be root:wheel, nonwritable by group/other)
EjectDelay
NoIdleSleepAssertion
batteryKioskModeData
NULL
Absolute
LatencyEventSystemOpen
HandleReportCnt
Can't create kext cache under %s - owner not root.
SampleInterval:
PM Notifications
LatencyEventSystemCreate
com.apple.hid.queueUsage
Personality CFBundleIdentifier names a kext that can't be found
droppedEvents
assertion failure: IODataQueueAllocateNotificationPort
(unknown object)\n
SCDynamicStoreSetValue
Key
DidStartLink
%@
IODeviceTree:/product
FromCorner 
Audio
_
DispatchQueue
Mkext length field %d does not match mkext actual size %d.
assertions
PerTaskAssertions
usagePage: %ld usage: %ld children: %ld ungroupForLegacy: %ld
caller
Can't create kext: missing or non-string CFBundleIdentifier in identifier cache entry %d.
Ungroup for legacy clients
Transition: None
IOHIDEventSystemClientNotifyDispatchMach
/AppleInternal/Library/HIDPlugins/ServiceFilters
%s:\n
wakepoweron
cancel
vendorUsagePage: %ld vendorUsage:%ld dataLength:%ld
com.apple.private.hid.client.service-protected
CP2520 Pattern 3
Wake On Clamshell Open
returnCode
SystemSleepPreventersWithID
Swipe
PropertyNotificationCount
IOHIDService.c
LatencySetProperty
(data object)\n
LastActivityTime
Extended
%s does not contain code for architecture %s.
com.apple.PowerManagement.control
com.apple.system.powermanagement.assertionresync
Bottom Button M4:
/IOKit/Power
assertion failure: CFMachPortCreateWithPort
Unable to determine realpath for %s - failing.
IOAVAudioInterface
initWithSession:
qos
Dolby Atmos (EAC3 7.1)
MaintenanceImmediate
Carrier Mode Low Voltage
userActivityRegister
Kext is a kernel component but OSBundleIsInterface is set to false; overriding
Failed to parse kernel log messages: %s.
ConfigurationDescriptors
com.apple.private.hid.client.event-filter.internal
HIDPreferencesCopyMultiple
Resting 
Normal
SetReportCallback
%s: %s - no such file or directory.
ValidPixelEncodings
Disk Sleep Timer
property
Sticky Key Toggle:
Performance_Warning
Reading resource file %s%s.
IsPreferred
AudioChannelLayoutElements
com.apple.private.hid.client.admin
HIDPointerButtonMode
com.apple.kext.unload
CVT
UserVisible
Kexts should declare dependencies on either com.apple.kernel* or com.apple.kpi.* libraries, not both.
Some dependencies are causing circular references
Reading loaded kext info from kernel.
/System/Library/Extensions
Mkext plist full size is %u.
EventSystemEntitlements
&gt;
Only incompatible kexts found for these libraries
<false/>
Humidity
filterEvent:toConnection:fromService:
Attempt to set 64-bit load address - %s.
filterEventMatching:event:forClient:
%3lld%c 
userActivityTimeout
Down:
Can't read running kernel architecture.
 (with termnation of IOServices)
Can't load %s - dependencies ineligible during safe boot.
%s.IOHIDManagerRef
LogLevel
Unknown CPU info given (type %d, subtype %d), using running kernel architecture %s.
AppleKernelExternalComponent
CH3:
CtrlKeyboardUsageMap
Kext library setting simulated safe boot mode to %s.
ConnectionPluginDebug
IOAVController
wakeData
HighFrequency
Monitor
_IOHIDServiceCreate_block_invoke
zlib inflateInit failed.
%s adding implicit KASan dependency
PID
MaxInputReportSize
%-20.20s 
EventType
Get Loaded Kext Info
Could not get absolute path of kext!
%s has no info dictionary; can't resolve dependencies.
Front Center High
WakeByCalendarDate
No load audit function set, cannot load %s
ElementData
DefaultConfiguration
%s%s
Realizing %s from identifier cache object.
_MKEXTExecutable
%dx%d%c %.3f Hz, %dbpc %s Range %s, %s colorimetry, %s EOTF
Stop 
CountryCode
%s - Interface kext must have exactly one dependency.
Can't load %s - authentication problems.
True
/System/Library/PrivateFrameworks/HIDAnalytics.framework/HIDAnalytics
FIXME: IOUnserialize has detected a string that is not valid UTF-8, \"%s\".
<true/>
assertionCheckToken
default
%-20.20s %ld\n
Sending all personalties for %s to the kernel.
Scanning %s for kexts.
Hibernate File
UUID
Info dictionary missing required property/value
Cache file %@ is out of date; not using.
OSBundleIsInterface
, no UUID
Physical Interconnect Location
IsLowPower
CalibrationDeadZoneMax
v24@?0^v8^v16
27:64
none
IO
Network-Root
Can't load %s - dependencies ineligible during safe boot:\n%@
Test Mode:    %d\n
eventCount
not
Can't load %s - failed to resolve dependencies based on loaded kexts.
vid 
.DS_Store
15:9
Master
DeviceOpenedByEventSystem
com.apple.iokit.statenotification.name
AmbientLightSensor
Direction Pad Up:
Failed to read kexts requested by kernel since startup - %s.
DP
propertyForKey:
AttributeDataLength:
AssertionOnBehalfOfPIDReason
serviceplugin
,
ClickSpeed:
Phase:
clientNotification:added:
Opening CFBundle for %s.
DolbyVision VSVDB
Collection
Not saving %s - read-only filesystem.
<string>typeID 0x%x not serializable</string>
TCCAccessPreflight
batteryHeatMapData
Reserved
%s has %d remaining undefined symbol%s
boolean, <true/> or <false/>
assertionFeatureSupported
IOHIDSystem
Saved cache file %s.
/System/Library/AppleUSBDevice/USBDeviceConfigurationOverride.plist
%s.IOHIDUserDeviceRef
%s%s (%s)%s
StopInfoFrame
Hibernate Free Time
Personality CFBundleIdentifier names a kext that doesn't declare an executable
Kext declares no com.apple.kpi.* libraries; if it references any kernel symbols, it may fail to link.
assertionCheckCount
oflag
64-bit kexts must use com.apple.kpi.* libraries, not com.apple.kernel* libraries.
%s has no executable for architecture %s.
DolbyVision (HDMI tunneling)
<key>
MaxState
connection_workloops
; reinitializing all kexts for new architecture
Resolving dependencies for %s.
%s - missing load info or dependencies array in applier function.
phase:
+
scRGB
CP2520 Pattern 1
IOPCITunnelCompatible
USB
SCPreferencesRemoveValue
EstimatedAzimuth 
activate
bootstrap_look_up2 failed with 0x%x\n
v28@?0Q8^{dispatch_mach_msg_s=}16i24
WillUpdateMask:
PropertyCache
TimingType
ConfigurationType
IOPathMatch
reason
ProtectLink
TCPKeepAlivePref
RunLoop
StageProgress:
Kexts already loaded for these libraries have no OSBundleCompatibleVersion
Kext identifier->path cache for %s - kext entry not a dictionary.
TimeoutTimeStamp
SCDynamicStoreNotifyValue
GenericGesture
CH0:
Terminate IOServices
assertionCreate
HIDPreferencesCopyDomainForInstance
bg 
IdleSleepPreventersWithID
activity
IOKit Power
Kext library %s using caches.
Failed to uncompress %s%s from %s.
Can't load %s - validation problems.
Sink
HIDPreferencesSetMultiple
%s%@%s
ATRAC
Branch
createOptions
SenderID:
B24@?0r*8^v16
EventLog
MPEG1
BT.2100 HLG
%g kHz %dch %d-bit %s
com.apple.PowerManagement
setProperty:forKey:
%c[1m
Decompress-only
size=\"%d\"
Locked
Bundle URL unexpectedly NULL!
HIDActivityState
SystemPowerProfileOverrideDict
RemoteActive
CH1:
Kext identifier->path cache for %s - base path missing or invalid.
Realpath for %s is %s
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
Transport
Running kernel architecture is %s.
8.0.0b1
Calculated
oversized
Timestamp type:
Joystick Axis X:
HIDDebug
com.apple.userspace_ethernet
Architecture %s not found by name, using running kernel architecture %s.
/Library/Extensions
6.0
AutoPowerOff Enabled
Standby Enabled
hid-workgroup-interval
Personality CFBundleIdentifier differs from containing kext's (not necessarily a mistake, but rarely done)
Pixel Clock:   %f Mhz (%u Hz)\n
service
Timing Attributes:\n
keyboardPress: %ld
DisplayIntegrated:
ThermalWarning
/System/Library/DriverExtensions
Decompress|Passthrough
LegacyBatteryInfo
DolbyVision (native)
chargeSocLimitIsEOC
Z:
IOHIDConnectionFilter
Send Resource
__kernel__
vendorID
DPCP
IOCircularQueueDescription
IOAccessoryBulkDataEndpoint
The kext contains a symlink which is either not readable or points outside of its bundle; please remove
SleepDisplay
ForceStage
Trying to authenticate kext with no authentication function, failing.
9:15
Tap
SupportsCollectionEvents
Can't read mach-o file %s.
AutoTimesout
InstanceMetadata
Hidden
serviceNotification:added:
LastActivityTimestamp
YES
_kmod_info
Downspread:    %s\n
1:1
AppleLSIFusionSCSI
ElementCookie
Joystick Axis Rz:
, DSC (%f bpp, decompress)
Twist:
UsagePercent
Compatible version must be lower than current version.
PowerManagement
Accelerometer
assertion failure: Dispatch queue already set
OSKextIdentifierCacheBasePath
Failed to send personalities to the kernel.
Scan Type:     %s\n
Display Sleep Timer
%-20.20s %qd\n
IOHIDService name:%s id:0x%llx primaryUsagePage:0x%x primaryUsage:0x%x transport:%s locationID:%@ reportInterval:%d batchInterval:%d events:%d mask:0x%llx sensorcontrols:%d
%@ -> %@ (kext is %@)
DTSHD
\"
32 Gbps (8Gbps/lane * 4 lanes)
Keyboard
DolbyVision LL YCbCr 4:4:4
PRBS7
poweron
Value
TiltX:
KEXT
Can't record kext in identifier lookup dictionary; no identifier.
SCPreferencesLock
VFTG
createPowerSource returned 0x%x\n
chargeSocLimit
HIDPropertiesRequiredForMatching
Can't rename temp cache file to %s - %s.
Loaded kext info:\n%s
Interlaced:    %s\n
HIDAnalyticsHistogramEventCreate
%c[0m
%-20.20s %s%s\n
Irregularity:
/usr/appleinternal/lib/HIDPlugins/ServicePlugins
SMPTE ST 2084 (PQ)
name
ForceActive 
Kext claims a shared executable with named kext, but that kext can't be found
IOClassNameOverride
Attribute 
NormalizedPositionX:
CapsLockDelayOverride
PortNumber
FIXME: IOCFSerialize has detected a string that can not be converted to UTF-8, \"%s\"
Timestamp
CalibrationSaturationMax
eventMask
AppleSecurityExtension
/Library/DriverExtensions
Manufacturer:
PolicyTimeoutTimeStamp
state.tags
batteryShippingChargeLimitAction
Behavior:
Load audit function returned false, bailing on adding %s to mkext.
IOUSBDeviceDescription
Compass
ColorComponent0:
IOHIDEventSystemClientDispatchQueue
QueueSize
LogIOHIDFilteredEvents
CPU_Power_Limits
Can't create kext: missing or non-string version in identifier cache entry %d.
/usr/appleinternal/lib/HIDPlugins/ConnectionPlugins
/System/Library/PowerEvents
Dependencies have incorrect owner/permissions
deviceClass
AppleLSIFusionSAS
IOProviderClass
Bluetooth
SwipeUp 
displayUUID
IODPController
IOPropertyMatch
DequeueTimestamp
%s/%s%@/%@%s%s%s
DisplayWake
Rear Left Center
HIDClickTime
%s.IOHIDDeviceRef:0x%llx
ProductID
Touch:
LastPropertyNotificationTime
Failed to close compression stream for %s - %s.
<array>
HIDPreferencesSet
PowerNap
<IOHIDDevice %p [%p]  'ClassName=%s'
MultiAxisPointer
Tap 
CountryCode:
assertionActiveAsyncByProcess
AppleEmbeddedSleepWakeHandler
Timestamp:
HandTapHold
Removing identifier->path cache %s.
StartInfoFrame
HIDKeyMapping
id
productString
batteryShippingChargeLimitEnable
ShipChargeLimitEnabled
Type
internal error
IOHIDFamily
 warnings
DownstreamFormat
plist
DoIdrefScan
%s adding implicit Kcov dependency
DroppedEventCount
VendorIDSource
ProbeScore
NTSC
CP2520 Pattern 2
<%s>
SCDynamicStoreKeyCreatePreferences
Failed to stop %s - %s.
original URL = \"%@\", 
Adding CFBundleIdentifier %s to %s personality %s.
VendorID:
Depth: [%d bpc] Encoding: [%s] Range: [%s] Colorimetry: [%s] EOTF: [%s] DSC: [%s]\n
IOHIDEventSystemClient State
Can't create kext from cache: %s is already open and has a different CFBundleVersion from identifier->path cache entry %d.
GoOffAndOnBus
All
MajorRadius:
IOHIDEvent Server Connection - Root
Info dictionary property value is of illegal type
Created mkext for architecture %s containing %u kexts.
Unsupported mkext version 0x%x.
SupportsDownspread
18 Gbps (6Gbps/lane * 3 lanes)
__unknown__
assertionRelease
&amp;
ForcePending 
ForceOffBusDisable
Encrypted
Reduce Processor Speed
Brightness
TouchSensitiveButton
Simple
PressCount
Creating kext with path %s.
loaded 
<integer> (kexts may not use <real>)
chargeSocLimitReason
Unknown
Category
AssertLevel
HIDResetPointer
net 
service.carplay
Identity 
ClientEventFilter
virtualServices
ReportInterval:
MinLinkRate
AC3
MP3
YCbCr 4:4:4
IsPowerOn
keeping
com.apple.system.powermanagement.SystemLoadAdvisory
Failed to get file info (stat failed)
Error uncompressing kext cache file %s - zlib returned %d - %s.
Get Loaded Kext Info By UUID
MaxPower
UTF32 Little Endian
!pthread_create(&__serviceRunLoop.thread, &attribute,(ThreadRoutine)&__IOHIDServiceRunLoopCompatibilityThread, NULL)
%s:\n\n
Ethernet
LastEventTime
Kext library recording diagnostics%s%s%s%s%s.
System Sleep Timer
Shoulder Button L2:
GetReportCnt
AllowMultipleCreates
Progress:
Flushing dependencies for all kexts.
Other
Info dictionary property value is illegal
Wake On Modem Ring
Repeat:
HIDServiceFilter
10:16
DVI
ReportInterval
WakeRelativeToSleep
batteryGaugingMitigationAction
Can't serialize personalities for %s.
begin
Services
ProximityDarkWake
HIDSessionFilter
:
Internal error; overrun mapping executable file %s.
AssertionOnBehalfOfPID
For loaded kext %s, v%s: no opened kext matches.
<dict>
IsVirtual
CompleteLink
ClickCount:
InterfaceRole
Kext logging %sabled for %s.
QueueState
/Library/Apple/System/Library/HIDPlugins/SessionFilters
setBatteryDofu
Format: %s Channels: %d SampleSize: %d SampleRate: %d hz\n
Standby Battery Threshold
alloc
assertion failure: Device has already been activated/cancelled.
msgCount
/System/Library/HIDPlugins/ServiceFilters
Wake On AC Change
Force
Saving cache file %s.
Failed to read loaded kext info from kernel - %s.
com.apple.iohidmanager
Can't read plist from cache file %s - %s.
Successfully unloaded %s.
IOAVVideoColorBitsPerPixel
SwipeDown 
UserKeyMapping
Can't create kext from cache: non-boolean OSKextEnableKextLogging in identifier cache entry %d.
BoundaryScroll
Up
fastpath
connection
Range 
ColorComponent2:
Can't serialize personalities.
v16@?0^v8
SecTaskGetCodeSignStatus
CPUPower
_MKEXTInfoDictionaries
SystemIsActive
Caller
HIDPreferencesSetDomainForInstance
SCPreferencesUnlock
ended
 authentication
WakeDisplay
14:9
/var/vm/sleepimage
ColorComponent1:
<OSKext %p [%p]> { 
Internal error in diagnositcs recording
Product Description
time of last save
assertionSetState
 
Can't create CFWriteStream to save cache %s.
Extracting %s%s from %s.
/Library/Caches/com.apple.xbs/CB3C5685-5D2F-4785-B125-00238CC55C5B/TemporaryDirectory.w7GqJC/Sources/IOAVFamily_user/IOAV.cpp
IOUSBDeviceController
%s not found in identifier lookup dictionary%s.
assertionUpdateActives
wake
AtmosphericPressure
com.apple.hid.analytics.service
kernelEventQueue
Number:
Link Training Data:\n\n
/System/Library/AppleUSBDevice/USBDeviceConfiguration.plist
Joystick Axis Z:
Protected
ReduceBrightness
gamingEnergyMode
Unregistered
restart
UPSShutdownAtMinutesLeft
CalibrationGranularity
kTCCServiceListenEvent
Not running as root; skipping save of identifier->path cache.
invalid pixel encoding
fd
com.apple.iokit.statenotification.create
IOHIDManager State
Began
Personality Names
Swing Voltage: %d\n
CoreGraphicsProgress
IODPPort
Flushing load info for all kexts (%s dependencies)
OSBundleStarted
 (kernel component)
HDMI
Shoulder Button R2:
StopLink
SecTaskCreateWithAuditToken
Matching
DTS
%s.%02X%02X%02X%02X-%02X%02X-%02X%02X-%02X%02X-%02X%02X%02X%02X%02X%02X
>
NSPrincipalClass
)\n
SCDynamicStoreCopyMultiple
SwipeLocked 
zlib deflate failed.
ProtectedServicesDisabled
Finger
0x%llx
No kexts found for these libraries
Interface kext must have exactly one dependency.
Finished reading identifier->path cache for %s.
batteryGaugingMitigation
Invalid
Kext declares both CFBundleExecutable and CFBundleSharedExecutableIdentifier; use only one.
Orientation usage:
IOClass
Compressed info dict from %u to %u bytes (%.2f%%).
plugin
TiltY:
sYCC601
PowerOnImmediate
TCCAccessRequest
<IOHIDConnectionFilterRef:%@>
__IOHIDEventSystemClientRefresh
Searching for link dependencies of %s.
OSBundleLoadSize
/AppleInternal/Library/Extensions
OSKext
{\n
OSKextSetTargetString
HIDScrollAccelerationType
/AppleInternal/Library/HIDPlugins/SessionFilters
assertionActivityUpdateRefCnt
Top Center
Default RGB
time
IOAVControlInterface
userEventQueue
Kernel load info for %s lacks a CFBundleVersion.
AssertReleaseWhen
Version:
AppleLSIFusionFC
UserInterfaceSupported
Reading load info for %u kext%s.
IOKitDebug
com.apple.private.hid.client.debug-tool.internal
UpstreamFormat
Sleep
Architecture %s not found in mkext.
kTCCServicePostEvent
Probability:
OSBundleDependencies
Slave
SystemPowerSettings
Adding %s to mkext.
MaxLinkRate
com.apple.system.IOPMSchedulePowerEventNotification
Power Management power source queue
%s, version %s removed from identifier lookup dictionary.
<integer>
SetDevicePreferredConfiguration
CEA
addStartTag
true
Standby Delay
shutdown
HIDCapsLockState
BundlePath
DSCRequiredColorElementIDs
IOCFSerializeBinary
setDispatchQueue:
Face Button B:
IOHIDService(%p) id:0x%llx name:%s
OSBundleLoadTag
NONE
assertionCopyActivityUpdate
EAC3
IOHIDQueue
Zoom
FluidTouchGesture
Bottom Button M1:
Kext Request Arguments
Failed to create lookup address object.
HDCP1
UsagePage
initWithService:
score
ConnectionEntitlements
(unknown)
Battery Power
kIOHIDServerConnectionRootQueue = hid_dispatch_pthread_root_queue_create(\"IOHIDEvent Server Connection - Root\", &attribute, NULL, 2)
Couldn't open CFBundle for %s.
HIDAnalyticsHistogramEventSetIntegerValue
Link Command
Kext identifier->path cache - kext info is not an array.
Failed to create directory %s - %s.
(invalid)
OSBundleWiredSize
%s - internal overrun in executable file (%s).
assertionAsyncOffloadDelay
Rear Left
...(%u bytes total)
/System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
Level:
Boot Level Restrictions
Can't read mkext fat header.
Action
Scale
Releasing CFBundle for %s.
com.apple.private.hid.client.event-dispatch.internal
.
hidsignpost
%-20.20s 0x%016llx\n
HeartRate
head
(kernel) %s
EnableIdleSleep
80-bit custom pattern
: 
Usage
---------------------------\n
HIDMouseScrollAcceleration
AssertType
DSC:          YES (%f bpp, decompress)\n
GRGB Tunneled as YCbCr422 (Even line blue)
isVirtualService
v24@?0r^v8r^v16
State
IOCFUnserialize: %s near line %d
UnifiedSleepSliderPref
%-20.20s %f\n
Removed %s, id %s%s, version %s.
0x%qx
status
batteryGaugingMitigationState
Confidence:
CFBundleIdentifier and CFBundleVersion must be < 64 characters.
Creating kexts from identifier->path cache for %s.
with
zlib inflate discrepancy, uncompressed size != original size.
Hibernate Free Ratio
Continuous
filterEvent:forClient:
FEC:           %s\n
Display Sleep Uses Dim
Enabled
IOPSPrivateBatteryHealthState
5:4
IOHIDSession - SessionEventDispatch
DCI-P3 (D65)
HIDPreferencesCopy
AutoPowerOff
IOHIDDeviceSuspend
SupportsEnhancedMode
ProtectedAccess
%s is a kernel component with no dependencies.
MinorRadius:
assertionWasCoalesced
WMAPro
Changed
Thermal_Level_Warning
 }
Can't load %s - no code for running kernel's architecture.
Relative
Path
FastSwipe 
Executable file doesn't contain kernel extension code (no kmod_info symbol or bad Mach-O layout).
Reading kext UUID for Address\n.
Minor
TTYSPreventSleep
\n
SampleInterval
com.apple.iohideventsystem
SystemTimeOutExpired
assertion failure: Queue already scheduled
<IOHIDEventSystem %p [%p]>{\n\tserviceDict=%@ \n\tnotificationDict=%@ \n\tmatchNotifySet=%@ \n\tclientSet=%@}
%@/%@
TimingStandard
Y:
Connections
Inactive
SCDynamicStoreCopyValue
.ioplist.gz
WillStopLink
IOCFSerialize
9:16
%-20.20s %llu\n
assertion failure: Client has already been activated/cancelled.
CASecureLayerOnScreen
assertion failure: IONotificationPortCreate
string
AID
FromEdgeFlat 
setProperty:forKey:client:
Product:
Pre-emphasis:  %d\n
&lt;
%s:%s%s%s%s%s%s%s
services
assertionUpdateCategoryPolicy
Vertical
SCDynamicStoreCreateRunLoopSource
%-25.25s %f\n
Failed to check path %s (CF error %ld).
IOHIDUserDeviceStateQueue
DolbyVision LL RGB 4:4:4
Full
Watch
.iohid
Link Rate:     %llu bps\n
%-20.20s %s\n
Flavor:
OSBundleRetainCount
com.apple.backboardd.hid
RetrainLink
Symbol Error Rate Measurement Pattern
DesktopModeAppliesOnBatteryPower
IOAccessoryIDBusBulkDataEndpoint
ColorSpace:
tail
Kext has no executable or compatible version, so it should not declare any OSBundleLibraries.
.XXXXXX
IOAVDisplayMemory
kr == KERN_SUCCESS
ReportDescriptor
Data:
IOHIDServiceFilter
com.apple.iohidmanager.uuid
 (dependencies not resolved).
XYZ
Class
LatencyServiceInit
Sending %d personalit%s to the kernel.
YCbCr 4:2:0
HIDInitialKeyRepeat
DYLD_IMAGE_SUFFIX
propertyForKey:client:
Failed to unload %s - %s.
AssertPID
HIDPointerAcceleration
NormalizedForceVelocity:
Failed to open CFBundle (unknown error).
Failed to remove identifier->path cache %s - %s.
UPSShutdownAfterMinutes
DidUpdateMask:
NormalizedPositionDeltaY:
0x0
kext
Failed to serialize data for cache %s.
%s created from m%s is missing its info dictionary.
NormalizedPositionDeltaX:
runloop
IOHIDNotification
Pressure:
W:
EstimatedPressure 
setEventDispatcher:
Cache file %@ is not a regular file; ignoring.
incompatible 
Passthrough-only
Automatic
workgroup_interval_force_disable
procName
Failed to read requests from kernel - %s.
String/URL conversion failure.
_MKEXTBundlePath
Dolby Atmos (MAT2.0)
SCDynamicStoreAddWatchedKey
PressCount:
SwipeLeft 
Face Button Y:
 ->
setting load address of %s to 0x%0x
com.apple.kpi.kasan
YCbCr 4:2:2 (DP tunneling)
Negotiating
filterEvent:
The booter does not recognize symbolic links; confirm these files/directories aren't needed for startup
%s has multiply defined %ld symbol%s
Command
matching
Upstream
Deprecated property (ignored)
X:
/System/Library/Caches/com.apple.kext.caches
ButtonMask:
DeviceUsagePairs
Root
%s has no personalities to send to kernel.
batteryChargingIconoGraphyState
IOEthernetController
Traditional gamma (SDR)
BSD Name
Wake On LAN
SystemSleepPreventers
Puck
Dependency lacks appropriate value for OSBundleRequired and may not be available during early boot
%@ is not a system extensions folder; not looking for a cache.
Can't load %s - a different %s is already loaded.
RGB 4:4:4
Carrier Mode High Voltage
IOKit Power Source Copy
chargeSocLimitSoc
ClearTime
The 'CFBundleIdentifierKernel' key is required in your personality to specify the base kext to load when your kext is instantiated.
Failed to read XML from mkext: %s.
Virtual:
FirstDroppedEventTime
IOCFUnserialize: can't alloc temp memory
IOHIDSessionFilter
IORequiredPacketFilters
trace
Range:
Encoding:
/Library/Apple/System/Library/Extensions
IOHIDConnection process:%@ pid:%d uuid:%@ caller:%@
IOHIDEventService
QueueCallbackTimestamp
promotable 
Attributes
IOAVVideoInterface
Split:         %s\n
16:9
%02x 
Can't parse info dictionary XML
Third-party Driver Extensions are ineligible to run in Safe Boot, or match on devices during early boot. Please remove the OSBundleRequired key from your Info.plist.
compatible 
assertionId
/usr/appleinternal/lib/HIDPlugins/ServiceFilters
IOService:/IOResources/IOHIDSystem
Kext is not signed
Clearing \"has all dependencies\" for %s.
Can't read file %s.
40 Gbps (10Gbps/lane * 4 lanes)
state.arrayIDRefDictionary
v12@?0I8
syntax error
assertion failure: Manager has already been activated/cancelled.
Rx:
IOHIDEventServer
workgroup_interval_force_enable
Underscan
Automatic Restart On Power Loss
chargeSocLimitDrain
IOUSBHostInterface
IOHIDEvent Interrupt - Root
OSKextVariantOverride
DroppedEventMask
135:256
size
assertion failure: Queue has already been activated/cancelled.
ForceOffBusEnable
IdleSleepPreventers
_MKEXTExecutableRelativePath
com.apple.powerd.assertionpolicy
TurnedOff
48 Gbps (12Gbps/lane * 4 lanes)
Events:
Can't open cache file %s, CF error %d.
Kext Request Predicate
cpu 
elementSetTime
%s has no symtab in its executable (%s)
TransducerType:
WakeImmediate
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n
Bottom Button M3:
Dependency Resolution Failures
Details
CarrierChargingMode
com.apple.system.powersources.timeremaining
_IOHIDLogCategory
CurrentBrightness:
Failed to map executable file %s (offset %lu, %lu bytes) - %s.
ProcessName
TPS3
LongPress:
Note: OSKextCopyKextsWithIdentifiers() - identifier %s not found.
Failed to load %s - %s.
256:135
scRGBfixed
EventMask:
Start 
LocationID:
%s: %lld\n
IONameMatch
userdevice
LED
SetReportCnt
ies
Sending named personalities of %s to the kernel:
propertyCacheHit
ShipChargeLimitData
Failed to lookup uuid with address from kernel - %s.
Peak 
assertionInitialConnection
Kexts may not use the DriverKit value for OSBundleRequired.
.plist.gz
Can't update mod time of cache file %s - %s.
PreciseAspectRatio
None
Rear Center
PropertyMerge
Reading cache file %s.
Fast:          %s\n
24 Gbps (6Gbps/lane * 4 lanes)
High Standby Delay
(date object)\n
LiftOffPredicted 
v48@?0^v8^v16^v24^v32^v40
lastNotifyEventTimeStamp
HIDIdleTimeMicroseconds
Vertical:      Total: %5u Active: %5u FrontPorch: %4u SyncWidth: %3u BackPorch: %3u SyncPolarity: %u PixelRepetition: %u SyncRate: %10.6f Hz\n
queueType
Location
VendorID
%-20.20s 0x%016llX\n
Generation:
Can't open CFBundle for %s.
Lane %d:\n\n
%-25.25s %d\n
Selectable
IOServicePublish
Kext library architecture set to %s%s.
Biometric
Kext identifier->path cache for %s is up to date.
OSBundleEnableKextLogging
Lane Count:    %d\n
Remove Child
? Gbps (Unknown FRL rate)
matchService:options:score:
Front Left High
Translation
Shoulder Button L1:
%s, version %s is already in the identifier lookup dictionary at index %d.
Omitting loaded kext %s from mkext for kernel load.
IOHIDEventSystemConnection uuid:%@ pid:%d process:%@ type:%s entitlements:0x%x caller:%@ attributes:%@ state:0x%x events:%d mask:0x%llx dropped:%d dropStatus:%d droppedMask:0x%llx lastDroppedTime:%@
(\n
Bottom Button M2:
HIDDefaultSensorControlOptions
MatchingEvent
Horizontal
Failed to open CFBundle for %s.
DeviceDescription
Authentication Failures
Checking CFBundle of %s for executable URL.
EventFilteredCount
LastDroppedEventTime
IOHIDLibPrivate.c
^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}16@?0^{os_state_hints_s=I*II}8
IOHIDService Enumeration - Root
IOUserEthernetInterfaceMergeProperties
Get All Load Requests
%@%s%s
Requests from kernel missing or of wrong type.
OSBundleRequiredPromotion
%-20.20s %-8llu %-8llu %-8llu %-8llu %-8llu\n
Stat failed for %s - %s.
com.apple.powermanagement.collectbt
Enhanced Mode: %s\n
AAC
HIDPreferencesCreateInstance
sentinel %qx\n
Personality %@ not found in %s.
com.apple.kernel
HIDAnalyticsEventCreate
Thumbstick Button Left:
TransitionTime,us:
Failed to start %s - %s.
AspectRatio
PowerByCalendarDate
dominoState
NavigationSwipe
HID - IOService Enumeration
Cache file %@ does not exist.
Get Kext UUID by Address
AssertionOnBehalfOfBundleID
AllowsDeviceRestart
SleepServices
CollectionCookie
Get Kernel Requests
%-20.20s %d\n
OSBundleLibraries
Revision
Requesting stop of %s.
ActivityLog
IOKitLib.c
Internal
/System/Library/HIDPlugins/ConnectionPlugins
%s: %s + %lu
%s has no Info.plist file.
Detailed
momentum:
com.apple.iohideventsystem.available
sleep
GenerationCount:
GetReportCallback
PrimaryUsage:
Video Link Data:\n\n
/IOKit/LowBatteryWarning
<off> 
MechanicalAngleDegrees:
Kernel request call returned no data.
Can't load %s - failed to resolve dependencies.
com.apple.iokit
TurnedOn
Motion:
OSBundleSharedExecutableIdentifier
, UUID 
batteryShippingChargeLimit
 (expected while realizing)
Down
(unknown error)
deviceProtocol
Scroll
Right Headphone
IOHIDEventSystem
HIDScrollAcceleration
Sticky Key Phase:
%p%p%p%p
/Library/Apple/System/Library/HIDPlugins
idRef
HIDKeyboardModifierMappingPairs
kern_result == KERN_SUCCESS
suspended
Flushing info dictionaries for all kexts.
```
