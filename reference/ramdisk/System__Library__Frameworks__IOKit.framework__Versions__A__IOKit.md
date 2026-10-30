# `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`

From the upgrade restore ramdisk (141-29011-104.dmg). 1,413,840 bytes.

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
assertion failure: \"pthread_mutex_unlock(&(service->queueContext)->lock)\" -> %llu
__IOMIGMachPortRelease mach_port_mod_refs:%s
IOHIDConnectionFilterCreate class does not conform to HIDConnectionPlugin protocol
IOHIDSessionCreate failed to find symbol %@ for bundle %@
IOHIDSessionUnregisterServices
IOHIDServiceFilterCreateWithClass Failed to find HIDServiceFilter protocol
Assertion 0x%x is neither active nor turned off
IOHIDService compatibility thread running at priority %d and schedule %d.
0x%llx: Start: %@
sendAsyncAssertionMsg failed: powerd xpc connection invalid
Failed to release assertion 0x%x on timeout
IOPMAssertionCreateWithProperties: io_pm_assertion_create failed with error 0x%x
0x%llx: kIOHIDResourceDeviceUserClientMethodHandleReport:%x
io_hideventsystem_remove_virtual_service:%x
HID Session async root queue running at priority %d and schedule %d.
IOHIDSessionRegisterFilters
%s: HIDVS ID:%llx iohideventsystem_client_dispatch_virtual_service_notification:%x
bootstrap_check_in() failed: %s
assertion failure: Failed to get async event source: 0x%x %p
Failed to create event at index=%d , eventDataSize: %u < sizeof(IOHIDEventData): %lu
Invalid SampleInterval: %@
Received a release not for gCurrentRemoteAssertion:0x%x. Received 0x%x
assertion failure: Activate failed queue: %p runLoop: %p
IOHIDSessionCreate
HID Event System Client refreshed with %ld services, cached matching had %ld services
IOCreatePlugInInterfaceForService:0x%x
0x%llx: set batch interval:%@ client:%@
Initial level is off for 0x%x: %@
Failed to create xpc reply object\n
HIDVS (id:%llx) invalid parameters
Invalid BatchInterval: %@
handleAssertionLevel: unable to find assertion with id 0x%x
IOObjectRetain:0x%x
Released connection: %s\n%{public}@
0x%llx: os_workgroup_interval_finish(cancel) error: %d, service %@
%s: iohideventsystem_client_dispatch_client_records_changed:0x%x
Session Filter:%@ filtered copy event (service:0x%llx, type:%d, new type:%d)
Update assertion policy %llu
Setting async client assertion id to 0x%x
Loaded %ld HID plugins (%@) %@
CreateSessionFilter
assertion failure: \"!manager->runLoop && !manager->dispatchQueue\" -> %llu
IOHIDEventServerCreate
__IOHIDServiceCreateObjcServicePlugin Failed to find HIDServicePlugin protocol
IOServiceMatchPropertyTable failed for url %@ for %@
Failed to create dictionary to send message\n
assertion failure: Invalid dispatch state: 0x%x
IOHIDEventSystemClose
assertion failure: \"pthread_mutex_init(&service->queueContext->lock, &mutexattr)\" -> %llu
HID Session async scheduling initiated.
HIDVS (id:%llx) client does not exist
level_change->true through kIOPMAssertionTimeoutKey write on an inactive assertion.
IOPMAssertionCreateWithProperties: pm connection failed
Loading symbol for principal class:%@ from bundle
IOHIDEventServerUnschedule
there is a timeout for category %@ and policy %@
Released assertion id gCurrentRemoteAssertion: 0x%x: 0x%x.Logging everything to powerd %@ %ld
0x%llx _IOHIDServiceCreate failed to load service plugin ret: 0x%x score: %d objcScore: %d
Loading session filter:%@
%s: Server died, preventing any future MIG calls
Connection added: %{public}@
0x%llx: IOHIDServiceSetElementValue time:%lluns
IOHIDSessionClose
0x%llx: kIOHIDResourceDeviceUserClientMethodPostReportResponse:%x
Sending initial message to powerd for async assertions
Event handler is called %@\n
__bootstrap_status:0x%x
IOHIDEventSystem TCC matching: could not load TCC.framework, gating disabled
__IOHIDServiceLoadObjcServicePlugin plugin did not provide passive matching dictionary %@
IOHIDSessionOpen
Connection: %@ not entitled to match protected service: %@
Successfully opened the IOHIDSession
_IOHIDCreateBinaryData: %@
onePlugin invalid for pluginType %@
%s
Invalid reply type\n
assertion failure: \"client->queuePort\" -> %llu
__IOHIDServiceCreateObjcServicePlugin class does not conform to HIDServicePlugin protocol
IOHIDEventSystemCreate
Virtual service (id: %llx) does not exist
Assertion 0x%x has already been released
Received assertion activity update refcnt %u overflow %d
0x%llx: IOHIDServiceRequestTerminate
__IOHIDServiceLoadServiceFilterBundles failed to find symbol %@ for bundle %@
%s: Event enqueue dropped:%d consecutive events
%s: mach_msg(sendPossiblePort):%s
Async assertion created with 0x%x, length %ld, %@\n
Invalid reply from PowerD\n
io_hideventsystem_do_client_refresh:0x%x
Error: the client with pid %d is missing the '%s' entitlement.
Failed to find %s for set, switch to default CFPreferences
io_service_t has no plugin for %@
Failed to create server dipatch queue
Connection: %@ TCC check for service %@: %@ returned right:%llu
Invalid type
CFDictionaryCreateMutableCopy fail
IOHIDSession close completed
Client record is not serializable for %@
Failed to find %s for synchronize, switch to default CFPreferences
assertion failure: \"pthread_mutexattr_destroy(&mutexattr)\" -> %llu
%s: mach_port_deallocate(unusedNotify):%s
offloadAssertions called with gCurrentRemoteAssertion 0x%x
Received active assertions from powerd %@
IOPMUnregisterNotification: cancelling connection 0x%lx\n
assertion failure: \"!queue->cancelHandler && handler\" -> %llu
__IOHIDEventSystemRelease
Connection: %@ denied match of service %@: TCC %@ right:%llu
%s: iohideventsystem_client_dispatch_service_removal:0x%x
Found timeout %@ for category string %@
Timeout is less than 0 %d
Sending assertion create msg for id 0x%x:%@\n
assertion failure: Schedule failed queue: %p runLoop: %p
processAssertionUpdateActivity unread-count %d
Assertion retain not supported in async mode\n
PowerD error: 0x%x\n
IORegistryEntryIDMatching:NULL
Set on screen cursor bounds px:%d py:%d minx:%d miny:%d maxx:%d maxy:%d
assertion failure: \"pthread_mutex_lock(&(session->queueContext)->lock)\" -> %llu
%s: mach_port_deallocate(notifyPort):%s
Failed to create gAssertionsDict
Assertion index 0x%x already exists
Failed to create dictionary to send message
Failed to find %s for set multiple , switch to default CFPreferences
failed to get interface for plugin for %@
Failed to register for reconnecting with powerd. rc:0x%x
HIDVS (id: %llx) invalid event data
Unable to create event queue via hidd: (%08x)
Service plugin %@: %@ never called cancel handler for service: %@
Entry of IOHIDService property %s incorrect type: %@
no factories for plugin for %@, kr = 0x%x, factories = %p, factoryCount = %ld
Client must be scheduled with dispatch queue or runloop
powerd returned assertion id 0x%x for async id 0x%x \n
Unable to allocate set client reply port attributes
bootstrap_look_up2 failed: %s
Unknown client type: %d pid:%d
IOPMAssertionCreateWithProperties: One of the arguments types is incorrect
IOServiceAddMatchingNotification:0x%x
Can not locate kernel service
%s: mach_port_allocate(sendPossiblePort):%s
%s: Filtered event type:%@ sender:%#llx eventInfo:(%@) -> outEventInfo: (%@)
%@ is not serializable
__IOHIDServiceLoadObjcServicePlugin failed to find symbol %@ for bundle %@
IOHIDSessionRelease
IOHIDSessionFiltersClose
0x%llx: Unable to create queue analytics
Unable to get serviceID for IOHIDServiceClient: %@
%s: HID activity: stop reporting
processAssertionTimeout: Removing from gActiveAssertionsDict: 0x%x
IOConnectGetService Failed with err : 0x%x
Received an error in response to copy '%s' data\n
Service: %@ cancellation timer timed out
HID Session async scheduling complete.
Could not find TCC symbol \"TCCAccessRequest\"
__IOHIDEventSystemCreateNotification
IOHIDEventSystemCreate error
Bad matching event
io_hideventsystem_create_virtual_service :%x
Failed to create gAssertionConnection\n
Failed to find %s for copy multiple, switch to default CFPreferences
IOServiceAddInterestNotification: 0x%x
0x%llx: __IOHIDUserDeviceStartDevice:0x%x
%s: HIDVS ID:%llx create
IOHIDEventSystem - enumeration queue termination
IOHIDServiceFilterCreateWithClass Failed to initialize filter
sendAsyncAssertionMsg failed: powerd xpc connection interrupted
Turning off assertion 0x%x: %@
Failed to create XPC message\n
IOHIDConnectionFilterCreate Failed to find HIDConnectionPlugin protocol
IOHIDEventSystemOpen error
IOHIDSessionUnschedule
Failed to convert CF dictionary to xpc object\n
API will be deprecated soon.  Please use IOHIDEventSystemClientCreate.
%s: Unable create activity notification
%s: HID activity: start reporting with interval: %ds
%s: HIDVS ID:%llx destroy
%s: HID activity: %d -> %d (service:0x%llx event:%d)
No policies defined for this process
Current assertion has been released by powerd gCurrentRemoteAssertion 0x%x gCurrentAssertion 0x%x
Bad matching dict
0x%llx: os_workgroup_interval_start error: %d, service %@
[%#llx] Invalid entitlements property, expected Array or String
Failed to get DeviceUsagePairs: %@
Setting Assertion State for PID %d to %d\n
Set fixed mouse location failed:0x%x
Failed to create event at index=%d , eventDataSize: %u < minimum size: %u for type: %u
0x%llx: unresponsive:%@ client:%@
__IOHIDServiceCreateObjcServicePlugin Failed to initialize plugin
Unable to serialize matching data
Checking for timeout for category %@ %d
plist invalid for pluginType %@
processAssertionUpdateActivity: No gAssertionConnection
handleAssertionLevel for 0x%x to %d: %@
Powerd has requested assertion activity update
Not a dictianary for 0x%x
No plist for plugin url %@ for %@
assertion failure: \"!device->cancelHandler && handler\" -> %llu
%s: mach_port_request_notification(MACH_PORT_NULL):%s
%s: %@ is missing the '%s' entitlement
assertion failure: Failed to create notification port %p
Assertion feature: setting gAsyncMode to %d
Service added: %{public}@
0x%llx: os_workgroup_interval_finish error: %d, service %@
0x%llx: IOServiceOpen:0x%x
Invalid ReportInterval: %@
Async assertion: setting offload delay to %llu
Failed to register for %s
Failed to create xpc msg object\n
Removing 0x%x from TimedList
fetchAssertionCategoryPolicies: Reply is not a dict
Category %@ has a policy %@
HID Event System Client refreshed but no services returned
Timeout from category %d
SetProperty called %@=%@ caller=%@
Category %@ not found
io_service_t has no IOCFPlugInTypes for %@
Recreating IOPMConnection id 0x%x\n
IOHIDEventSystem TCC matching: SecTask code sign status SPI unavailable, gating disabled
assertion failure: \"pthread_cond_init(&session->stateCondition, ((void*)0))\" -> %llu
%s: iohideventsystem_client_dispatch_properties_changed:0x%x
invalid io_service_t for %@
Failed to create XPC connection to PowerD\n
CreateSessionFilterClass
Could not find TCC symbol \"TCCAccessCheckAuditToken\"
Created IOPMConnection with id 0x%x\n
assertion failure: \"__IOHIDQueueSetupAsyncSupport(queue)\" -> %llu
IOHIDEventSystemOpen:%lldus
Unable to allocate client reply port
Unable to allocate acquire client reply port attributes
posting reset to (%p)(%p, %p)
Failed to create xpc connection
IOHIDEventSystem TCC matching: could not load Security.framework, gating disabled
Bad arguments
%s: iohideventsystem_client_dispatch_event_filter:0x%x
Replying to assertion check message with count %d token:%llu\n
%s: Unable to create activity timer
EventToConnection filtered type:%d service:0x%llx connection:%@ session filter:%@
0x%llx: Packet size is to small for large report, but large report flag is set. reportFlags:%#x entrySize:%u
probe failed for plugin for %@
Unable to create event attachment storage
IOHIDSessionFilterCreateWithClass failed for bundle %@
Checking getTimeout for string %@
Set cursor enable:%s
0x%llx: set report interval:%@ client:%@
%@ is not serializable. result: %@
%s: Unable to create DISPATCH_SOURCE_TYPE_MACH_SEND for reply port
Failed to find %s for set domain, switch to default CFPreferences
Failed to convert XPC to CF object\n
0x%llx: IOHIDResource not found
FilterEvent filtered type:%d service:0x%llx eventInfo:(%@) session filter:%@
0x%llx: __IOHIDServiceInit creating queue with high-priority QOS
No timeout for category %@ for policy %@
0x%llx: unschedule from dispatch queue completed
unable to make mach memory entry. (%08x)
offloadAssertions fired
Powerd has requested active assertions update
Failed to register for server availability: %d
io_hideventsystem_queue_start:%#x
0x%llx: unschedule from runloop completed
Sending Assertion release message for assertion Id 0x%x\n
Irrecoverable error for assertion creation\n
IOHIDSessionFilterCreateWithClass Failed to find HIDSessionFilter protocol
Failed to create message\n
Received an error in response to copy scheduled wake data\n
Connection removed: %{public}@
Unable to map event queue: (%08x)
Failed to create xpc reply object
IOCreatePlugInInterfaceForService:0x%x for serviceID:%#llx
All actions on server queue completed.
IOHIDEventSystemServer died. Reestablishing connection.
Copy Event filtered type:%d sender:0x%llx eventInfo:(%@) service filter:%@
%s: mach_port_deallocate(oldNotify):%s
%s: Event latency:%lld type:%d sender:0x%llx
No assertion dictionary or logging data to send
Suspending timer
CFPlugInCreate failed for url %@ for %@
Service removed: %{public}@ %@
Assertion has a policy category timestamp %@
IOHIDEventSystemCreate:%lldus
[%#llx] Invalid kIOHIDTCCServiceKey property, expected String
%s: HIDVS ID:%llx iohideventsystem_client_dispatch_virtual_service_copy_property:%x
setAsyncAssertionProperties for 0x%x %@:%@
0x%-16llx 0x%-16llx 0x%-16llx 0x%-16llx 0x%-16llx
assertion failure: \"client->notifyPort\" -> %llu
0x%llx: IOHIDService property %s incorrect type: %@
thread_id=%p
Not a dictinary for 0x%x
processAssertionTimeout: Turning off assertion idx:%d id:0x%x
%s: HIDVS ID:%llx iohideventsystem_copy_matching_event_from_virtual_service:%x
Received processCheckAssertionMsg with active assertion 0x%x
Timeout: assertion id 0x%x with time %llu, policy timeout %llu
_IOHIDCreateBinaryData fail
Failed to create event at index=%d , eventDataMaxSize: %u < eventDataSize: %u
0x%llx: Destroy: %@
QueryInterface:%x
IOPMAssertionCreateWithName: One of the arguments is NULL
Failed to create CF properties: 0x%x\n
HIDVS (id:%llx) does not exist
%s: mach_port_request_notification(notify) unexpected old notify port %#x
Re-syncing assertions
Failed to send mach port for IOPMConnection id 0x%x. rc:0x%x\n
IOHIDServiceFilterFilterSetPropertyForClient %@  %@ -> %@ filter:%@
IOHIDEventSystemServiceRemove
assertion failure: \"pthread_mutexattr_init(&mutexattr)\" -> %llu
assertion failure: \"pthread_mutex_unlock(&(queueContext)->lock)\" -> %llu
Malformed PropertyMerge value in bundle: %@
createAsyncAssertion: async mode disabled due to SmartPowerNap
IOPMUnregisterNotification: no valid ref for 0x%lx
Insufficient permissions to set kIOHIDSessionCASecureLayerOnScreenKey for UUID: %@
assertion failure: IOConnectMapMemory:0x%x
Powerd knows about this assertion 0x%0x. let powerd time it out
Received an error in response to copy assertion activity
Unable to open %#x
Service:0x%llx  is unregistered, not matching
%s: HIDVS ID:%llx iohideventsystem_output_event_to_virtual_service:%x
Failed to find %s for create
Unable to create IOHIDEvent with length:%d
Failed to register for reconnect with powerd 0x%x
No AssertionActivity in xpc reply
Fail to set parameter with status 0x%x
called with a NULL callback
Unable to serialize event
io_hideventsystem_dispatch_event_for_virtual_service:%x
insufficient buffer data available, size: %ld, length: %ld
%s: HIDVS ID:%llx Invalid parameters: key:%@
gAsyncModeDisableOverride: enable
start failed (%s) for plugin for %@
%@
%s: HIDVS ID:%llx: iohideventsystem_client_dispatch_virtual_service_set_property:%x
IOHIDConnectionFilterCreate Failed to initialize plugin
0x%llx: Set batch interval current:%d new:%d result:%d
Failed to get PM queue\n
0x%llx: IOServiceAddInterestNotification 0x%x
%s: Connection filter added:%@
Initial connection to powerd not setup
Received assertion category policies from powerd %@
Unexpected data type in gAssertionsDict for id:0x%x\n
Logging all %ld activity to powerd\n
pluginPath == NULL, unable to allocate a CFString
Missing state in reply\n
assertion failure: \"pthread_mutex_unlock(&(session->queueContext)->lock)\" -> %llu
Unable to create queue analytics
Releasing assertion locally id 0x%x
Failed to create the remoteID to CF for id %@\n
processCurrentActiveAssertions: No gAssertionConnection
Failed to create IOPMConnection. rc:0x%x\n
Unable to allocate queue object via _CFRuntimeCreateInstance
processAssertionTimeout: Removing idx:%d id:0x%x
Failed to create ASBM services\n
Enabled flag not found\n
assertion failure: \"pthread_mutex_lock(&(service->queueContext)->lock)\" -> %llu
_releaseAsyncAssertion: Failed to get the assertion details for id:0x%x\n
Received termination imminent error for connection 0x%lx
IOHIDEventCreateDigitizerEvent event is null
IOHIDEventSystemAddServices
Service filter %@ never called cancel handler for service %@
%s: Sent client refresh msg, status:%#x
XPC event: %@\n
Unable to create analytics description
Missing key '%s'\n
Failed to create xpc objects to send userActivityRegister message\n
%s: mach_port_request_notification(notify):%s
No category
Setting gAssertionsOffloader timeout to %llu\n
Failed to create event system client
IOHIDEventSystemRelease
Creating deep copy of record belonging to service: %@
EventForClient filtered type:%d sender:0x%llx eventInfo:(%@) service filter:%@ for client:%@
IOPMAssertionCreateWithProperties: Failure copying assertion properties. Collect backtrace %llu
bundle invalid for pluginType %@
Failed to get UUID. rc=%d\n
Failed to create connection\n
unable to create dictionary
%s: iohideventsystem_client_dispatch_notification_results:0x%x
No current assertion. Sending all activity till now
CFPlugInFindFactoriesForPlugInTypeInPlugIn failed for plugin url %@ for %@
Set on screen cursor bounds failed:0x%x
Failed to update machport for IOPMConnection id 0x%x. rc:0x%x\n
All actions on enumeration queue completed.
Add filter:%@ for service:0x%llx
%s: Event enqueue error:0x%08x type:%d sender:0x%llx
gAsyncModeDisableOverride: disable
Registering for assertion policy changes
mach_port_deallocate(server_port) %s
0x%llx: Failed to open service
assertion failure: \"pthread_mutex_init(&session->queueContext->lock, &mutexattr)\" -> %llu
Invalid ptr=%p size=%d.
level_change through kIOPMAssertionLevelKey write.
Fail to get parameter with status 0x%x
assertion failure: \"retainCount < (2147483647 *2U +1U)\" -> %llu
HIDVS (id: %llx) does not exist
setAsyncAssertionProperties: Failed to get the assertion details for id:0x%x\n
handleAssertionTurnOff: Released assertion id 0x%x
IORegistryEntrySetCFProperty Failed for kIOHIDActivityUserIdleKey with err : 0x%x
Service: %@ trigger matching failed: service is already registered
IOHIDSessionCreate - Load bundles
No timeout ts. Remove from timed list
logAsyncAssertionActivity: unable to find assertion with id 0x%x
failed to create instance for plugin for %@
unregisterNotification: invalid ref to 0x%lx
Set cursor bounds minx:%d miny:%d maxx:%d maxy:%d
IOHIDSessionFilterCreateWithClass class does not conform to SessionFilter protocol
Failed to create PM queue\n
restore property %@ to %@
assertion failure: \"pthread_mutex_lock(&(queueContext)->lock)\" -> %llu
0x%llx: IOHIDUserDevice start failed:0x%x properties:%@
0x%llx: Unable to create analytics description
IOHIDServiceFilterCreateWithClass class does not conform to HIDServiceFilter protocol
Unexpected message from async assertions connections\n
XPC event handler: %@\n
Failed to create useractiveRefs
Add session filter:%@
IOHIDSessionSchedule
Setting assertion timeout to fire in %d msecs for timeout_ts %llu
unexpected policy request %llu
0x%llx: get report not handled
Setting category timeout timestamp to %@, monotonic time %llu
io_service_t has invalid IOCFPlugInTypes for %@
IOHIDEventSystem TCC matching: tcc_authorization_check_audit_token unavailable, gating disabled
Event filtered type:%d sender:0x%llx eventInfo:(%@) service filter:%@
%s: mach_port_deallocate(reply_port):%s
Assertion has a category %@
Assertion 0x%x not found to activate
IOPMAssertionCreateWithProperties: One of the arguments is NULL
Session Filter:%@ filtered copy event (service:0x%llx, type:%d)
Set cursor enable failed:0x%x
assertion failure: \"queuePort\" -> %llu
handleAssertionTimeout fired %llu
Failed to create XPC connection\n
Shipping charge limit data not found\n
assertion failure: \"semaphore\" -> %llu
0x%llx: Set report interval current:%d new:%d result:%d events:%@
Could not find TCC symbol \"TCCAccessPreflight\"
event system =\n%s
io_hideventsystem_set_properties:0x%08x result:%d
Failed to find %s for copy domain, switch to default CFPreferences
IOHIDServiceFilter cancel handler invoked more than once for filter:%@
processAssertionTimeout: Not found in gActiveAssertionsDict: 0x%x
handleAssertionTimeout: Setting assertion timeout to fire in %llu secs
[%s] Process has entitlement %s on Non-Internal build
Resuming timer
IOHIDConnectionFilterCreate failed to find symbol %@ for bundle %@
No connection to powerd
IOPMAssertionCreateWithProperties: Call to io_pm_assertion_create failed with kernel error 0x%x
QueryInterface(kIOHIDDeviceDeviceInterfaceID):0x%x
IOHIDEventSystemOpen
mach_port_deallocate(bootstrap_port) %s
Unable to retain service: 0x%x
%s: HIDVS ID:%llx _iohideventsystem_copy_event_from_virtual_service:%x
xpc_user_sessions_get_foreground_uid failed: %d - %s
Failed to create event at index=%d eventCount=%d eventDataOffset=%d lenght=%ld
IOHIDServiceFilterCreateWithClass failed for bundle %@
CopyServiceRecords deep copy failed. Service record for %@ is not serializable.
IOServiceGetMatchingServices:0x%x
Received an error in response to IOPMCopyActiveAsyncAssertionsByProcess
powerd released our connection
Failed to load %s
Could not load TCC
Wake progress from %d. data: 0x%x\n
no event->parent->eventData
assertion failure: Failed to get queue port %p %p
SecTaskCreateWithAuditToken failed for pid:%d
IOHIDEventSystem - service queue termination
invalid matching dictionary: %@
0x%llx: close completed
IOHIDEventQueueNotify:%#x
assertion failure: Unschedule failed queue: %p runLoop: %p
No assertions by process
0x%llx: set property:%@ value:%@ client:%@
Failed to find %s for copy, switch to default CFPreferences
IOHIDSessionFilterCreateWithClass Failed to initialize filter
0x%llx: set report not handled
assertion failure: Cancel failed queue: %p runLoop: %p
powerd returned err 0x%x to create assertion %@. Dropping the assertion\n
assertion failure: \"retainCount\" -> %llu
IOHIDEventSystemAddService
HIDVS (id:%llx) invalid property key
Async sssertion bufffer initialized.
Set cursor bounds failed:0x%x
Received connection invalid error for connection 0x%lx. UnregisterNotification
Failed to send IOPMConnection request. rc:0x%x\n
assertion failure: \"completionElement\" -> %llu
assertion failure: \"!manager->cancelHandler && handler\" -> %llu
bootstrap_look_up_per_user failed: %s
 
/IOKit/LowBatteryWarning
Ended
setHIDEventService:
Can't stat path %s - %s.
Can't read plist from cache file %s - %s.
Internal error in diagnositcs recording
MPEG2
IOHIDEvent
%-20.20s %qd\n
NaN
IOHIDService - RunLoopCompatibilityThread
DisplayIntegrated:
MechanicalAngleDegrees:
CPUPower
Send Resource
FirstDroppedEventTime
DSC:          YES (%f bpp, decompress)\n
Vertical:      Total: %5u Active: %5u FrontPorch: %4u SyncWidth: %3u BackPorch: %3u SyncPolarity: %u PixelRepetition: %u SyncRate: %10.6f Hz\n
BT.2020 (YcCbcCrc)
Hidden
xvYCC709
chargeSocLimit
SecTaskCreateWithAuditToken
%s: %s + %lu
Can't read kernel CPU info from IORegistry (absent or wrong type).
BatteryPacks
batteryHeatMapData
QueueSize
DeviceOpenedByEventSystem
TPS2
HIDKeyMapping
IOClass
Loaded kext info from kernel is wrong type.
com.apple.kpi.unsupported
HIDAnalyticsEventSetIntegerValueForField
HIDPreferencesCopyMultiple
CEA
File owner/permissions are incorrect (must be root:wheel, nonwritable by group/other)
Scanning %s for kexts.
/usr/appleinternal/lib/HIDPlugins/SessionFilters
LastPropertyNotificationTime
KextIdentifiers
Can't create kext from cache: %s is already open and has a different CFBundleIdentifier from identifier->path cache entry %d.
FIXME: IOCFSerialize has detected a string that can not be converted to UTF-8, \"%s\"
%-20.20s 0x%08x\n
Touch:
Passive
DeviceUsage
IOHIDDeviceDispatchMach
Can't create CFWriteStream to save cache %s.
HIDPreferencesCopyDomainForInstance
com.apple.system.powermanagement.assertionresync
RemoteActive
Executable file doesn't contain kernel extension code (no kmod_info symbol or bad Mach-O layout).
zlib deflate failed.
batteryGaugingMitigationAction
Creating kext with path %s.
CFBundleIdentifier
Dynamic Range & Mastering
key
UnsafeColorElementIDs
Data:
SystemIsActive
DCI-P3 (Theater)
WakeRelativeToSleep
HIDNumLockState
%-20.20s 0x%x\n
DolbyVision (HDMI tunneling)
}\n
SymbolicHotKey
ServiceID
suspended
eventMatching:forClient:
setting load address of %s to 0x%0llx
%s is not valid; omitting from mkext.
Sleep On Power Button
8.0.0b1
Attributes
Physical Interconnect Location
Date of first use
Azimuth:
UTF16 Big Endian
Cache file %@ does not exist.
Failed to lookup uuid with address from kernel - %s.
%s - loaded dependency %s lacks valid OSBundleCompatibleVersion.
Major
ProductID
Kext identifier->path cache for %s - version %d unsupported.
OSBundleLibraries
HIDAnalyticsHistogramEventSetIntegerValue
24 Gbps (6Gbps/lane * 4 lanes)
IOAVAudioInterface
CompleteLink
not serializable
%s.IOHIDManagerRef
Tap 
AllowsDeviceRestart
MPEG
UPS Power
NormalizedPositionY:
SetReportCnt
Adding %s to mkext.
Format: %s Channels: %d SampleSize: %d SampleRate: %d hz\n
Underscan
IOService:/IOResources/IOHIDSystem
CalibrationMin
DeviceUsagePage
A system kext has a property set that it shouldn't
    
MaxLaneCount
4:5
chargeSocLimitDrain
a
com.apple.kernel.unsupported
Timing Attributes:\n
ValidPixelEncodings
Inhibit
IOPCITunnelCompatible
 = 
Begin
IOHIDEventService
com.apple.private.hid.client.event-monitor
3:4
IOHIDSessionFilter
Timestamp:
initWithService:
MotionActivity
PerformanceWarning
Can't determine actual safe boot mode - sysctl() failed for KERN_SAFEBOOT - %s.
%s - no compatible dependency found for %s.
Humidity
Identity:
ClientRecords
__kernel__
VGA
BoundaryScroll
Indirect dependencies can't be resolved
no
***UNKOWN***
Can't update mod time of cache file %s - %s.
SystemTimeOutExpired
Link Mode:    %s\n
HIDAnalyticsEventAddField
<string>typeID 0x%x not serializable</string>
batteryShippingChargeLimit
VendorID
com.apple.hid.queueUsage
Kext contains symlink at %s which points outside of its bundle at %s; rejecting.
Encrypted
Can't serialize personalities.
/System/Library/HIDPlugins/ServiceFilters
SystemPowerSettings
Info dictionary property value is of illegal type
Can't read mach-o file %s.
ClientSuspend
LongSqueeze
DequeueTimestamp
LoginWindowProgress
Puck
<IOHIDConnectionFilterRef:%@>
assertionRelease
ServiceEntitlements
com.apple.backboardd.hid
AppleEmbeddedSleepWakeHandler
OSBundleCPUSubtype
OSBundleLoadSize
AssertionOnBehalfOfPIDReason
HIDPreferencesCopyDomain
%p%p%p%p
Personality matches on IOResources but IOMatchCategory is missing or not equal to its IOClass; driver may be blocked from matching or may block others
NameChange
%s.%02X%02X%02X%02X-%02X%02X-%02X%02X-%02X%02X-%02X%02X%02X%02X%02X%02X
Face Button Y:
HIDServiceFilter
ConnectionEntitlements
StopInfoFrame
OSBundleRequired
PerTaskAssertions
<true/>
notificationCount
AllowMultipleCreates
Dolby Atmos (EAC3)
32 Gbps (8Gbps/lane * 4 lanes)
rh:
SupportsCollectionEvents
No load audit function set, cannot load %s
StandardType:
/System/Library/HIDPlugins/ServicePlugins
NTSC
/var/vm/sleepimage
CoreDisplayProgress
IODPPort
Get Kext UUID by Address
createPowerSource returned 0x%x\n
AbsentWithDisplay
BuiltIn:
LatencyCopyProperty
Kext identifier->path cache for %s is up to date.
reason
Altitude:
IOCFSerialize
TTYSPreventSleep
FromCorner 
Ry:
Direction Pad Down:
IOHIDService Enumeration - Root
OSKextSetTargetString
non
Reading kext UUID for Address\n.
Can't read file %s.
Traditional gamma (HDR)
scRGBfixed
DVI
WakeImmediate
HIDResetKeyboard
Undefined
Dependency Resolution Failures
Failed to create directory %s - %s.
(executable from mkext)
Joystick Axis Rz:
Count:
IOHIDConnectionFilter
dext
On
com.apple.system.powermanagement.SystemLoadAdvisory
assertion failure: Device already scheduled
VendorDefined
Pressure:
HIDPropertiesRequiredForMatching
9:16
HIDKeyboardModifierMappingSrc
Releasing CFBundle for %s.
FEC:           %s\n
RGB 4:4:4
SleepServices
IOBatteryInfo
Joystick Axis Y:
assertion failure: IONotificationPortCreate
com.apple.private.hid.client.service-protected.internal
ReprotectLink
IOPacketFilters
Finger
Level:
IOHIDFamily
eventCount
net 
Can't read mkext fat header.
HIDAnalyticsHistogramEventCreate
Failed to map executable file %s (offset %lu, %lu bytes) - %s.
 (expected while realizing)
Dolby TrueHD (MAT1.0)
set
%-25.25s %f\n
IOUSBDeviceController
%s has no executable for architecture %s.
IdleNotificationTime
IOUserEthernetResource
com.apple.kpi.private
EjectDelay
/Library/Caches/com.apple.xbs/CB3C5685-5D2F-4785-B125-00238CC55C5B/TemporaryDirectory.w7GqJC/Sources/IOAVFamily_user/IOAV.cpp
DeepSleep
Reading loaded kext info from kernel.
TPS1
com.apple.iokit.statenotification.set
Display Sleep Uses Dim
HIDInitialKeyRepeat
DeviceUsagePairs
elementSetTime
IOPersonalityPublisher
AssertReleaseWhen
Embedded
%-20.20s %llu us\n
Created
DolbyVision LL YCbCr 4:2:2 (DP tunneling)
%s:%u: %s(): %s
\"
setPowerSourceDetails returned 0x%x\n
NULL
Identity 
ProtectedAccess
Personality CFBundleIdentifier names a kext that can't be found
TPS4
VAC-T
Running kernel architecture is %s.
%s, version %s removed from identifier lookup dictionary.
EventSystemEntitlements
Y:
OSBundleSharedExecutableIdentifier
ConnectionPluginDebug
chargeSocLimitSoc
NextEventTimeStampDelta
Can't parse info dictionary XML
AssertStartWhen
Vendor Specific Data Block
Sink
disk 
%-20.20s %-8llu %-8llu %-8llu %-8llu %-8llu\n
Hibernate Free Time
workgroup_interval_force_disable
Get Loaded Kext Info By UUID
assertionCheckToken
forward reference detected
HIDClickSpace
.
%-20.20s %@\n
PressedThreshold:
Compressed write error for cache file %s - %s.
DolbyVision LL YCbCr 4:2:2
HIDPreferencesSet
IOService:/
setDispatchQueue:
Down
MaxPropertyGetTime
HumanReadableReason
DYLD_IMAGE_SUFFIX
%-20.20s %d\n
Joystick Axis Z:
timeout
Default RGB
Type:
TransitionTime,us:
<%s IDREF=\"%d\"/>
/Library/DriverExtensions
%s: internal overrun (%p, string_index: %d, file_end: %p) in executable file (%s).
Revision
LatencyEventSystemCreate
Simple
IOEthernetController
<array>
%s%@%s
v16@?0r^v8
Face Button B:
com.apple.hid.analytics.service.dispatchEvent
getBatteryHealthState
Temperature
Can't stat source folders for cache file %@.
time of last save
Squeeze
Info dictionary property value is of incorrect type
/System/Library/PrivateFrameworks/HIDAnalytics.framework/HIDAnalytics
Enabled
Accelerometer
IONetworkInterface
AdobeRGB
LowPowerMode
Velocity
------------------------\n
EventLog
UpdateLink
memory exhausted
DisplayIntegrated
IOUserClass
HIDScrollAccelerationType
DoIdrefScan
%@%s%s
v8@?0
%-20.20s\n
IOHIDService(%p) id:0x%llx name:%s
Driver Extension lacks appropriate value for OSBundleRequired, and will not be launched without kextd present. Use one of 'DriverKit' or 'Safe Boot.'
Unable to determine realpath for %s - failing.
Recorded %s%s, id %s, version %s.
Slave
cursor
isVirtualService
size
systemAssertionTimeout
EventFilterTimeoutCount
powerInfoPrecise
Flavor:
assertionCopyActivityUpdate
configurations
GoOffAndOnBus
Protected
oversized
phase:
IOUSBDeviceData
Safe Boot
com.apple.private.hid.client.motion-event-privileged
state.tags
Pointer
HIDServicePlugin
OSKernelCPUType
Cache file %@ is not a regular file; ignoring.
OSBundleCPUType
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
RestartAfterKernelPanic
Timestamp type:
com.apple.private.hid.client.event-dispatch.internal
Rear Left
PresentActive
Type
Can't unserialize kext request response: %s
com.apple.private.hid.client.event-filter
Sequence:
SensorPropertySupported
%@%@/%@
aud 
wakeData
Digitizer
Get All Load Requests
StartInfoFrame
Protection Command
connection_workloops
PropertyMerge
ServiceRecords
%s: %lld\n
HDCP2
dict
Wake On LAN
WakeByCalendarDate
com.apple.kext.load
Horizontal:    Total: %5u Active: %5u FrontPorch: %4u SyncWidth: %3u BackPorch: %3u SyncPolarity: %u PixelRepetition: %u SyncRate: %10.6f kHz\n
CP2520 Pattern 3
Carrier Mode High Voltage
/System/Library/PowerEvents
FastSwipe 
Get Loaded Kext Info
Unsupported
Decompress-only
27:64
IOCFPlugInTypes
AutoPowerOff Delay
com.apple.system.accpowersources.timeremaining
openOptions
HIDParameters
Repeat:
Behavior:
userEventQueue
TurnedOff
HIDPreferencesSetMultipleForInstance
ElementCookie
TiltX:
CreatorBacktrace
>
Unicode
Top Center
D10.2
SCPreferencesRemoveValue
CalibrationSaturationMin
Joystick Axis X:
ServicePluginDebug
en
IOResources
IsPreferred
Matching
matchService:options:score:
assertionProperties
Downspread:    %s\n
ID
com.apple.system.accpowersources.attach
propertyCacheHit
AtmosphericPressure
DefaultDeviceDescription
addStartTag
Supported Features
userActivityTimeout
LatencyServiceInit
Dolby Atmos (EAC3 7.1)
48 Gbps (12Gbps/lane * 4 lanes)
Power
TiltY:
Successfully stopped %s.
AsyncClientAssertionId
IORequiredPacketFilters
(unknown object)\n
NotificationActive
EventTypeCounts
Can't create kext from cache: %s is already open and has a different CFBundlePackageType from identifier->path cache entry %d.
SMPTE ST 2084 (PQ)
HIDPreferencesSynchronize
assertion failure: Dispatch queue already set
%@/%@
OSBundleLoadAddress
IOHIDServiceFilter uuid:%@ name:%@ %@
Link Rate:     %llu bps\n
Key:
LatencySetProperty
Orientation usage:
kIOHIDServerConnectionRootQueue = hid_dispatch_pthread_root_queue_create(\"IOHIDEvent Server Connection - Root\", &attribute, NULL, 2)
head
Kext declares no com.apple.kpi.* libraries; if it references any kernel symbols, it may fail to link.
leeway
uuid
AC Power
d
Extra Button L4:
IOHIDEvent Interrupt - Root
should be %s
com.apple.powerd.assertionpolicy
Scan Type:     %s\n
LED
%-20.20s 0x%016llX NON KERNEL SENDER\n
Display Sleep Timer
SCDynamicStoreCopyMultiple
^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}16@?0^{os_state_hints_s=I*II}8
/AppleInternal/Library/HIDPlugins
Vertical
Dynamic Power Step
HIDSubinterfaceID
begin
with
TrainLink
ZoomToggle
HIDKeyboardModifierMappingPairs
RegistryID
kext
Vendor Specific
HIDServiceSupport
setOutputEvent:
(kernel) %s
%@
onenessState
ReportDescriptor
msgCount
Libraries declared for both com.apple.kernel and a com.apple.kernel.* component.
Can't load %s - failed to resolve dependencies based on loaded kexts.
%s: %lld.%0*lld\n
Protection Command (with source and AUP data)
CalibrationGranularity
Successfully unloaded %s.
Can't read loaded kext info - current architecture %s != kernel's architecture %s.
DSC:          NO\n
YCbCr 4:2:0
false
UpstreamFormat
1.2.12
NONE
Rate:
%c[1m
UserInterfaceSupported
Network-Root
TPS3
IOKit.framework:IONotificationPortGetRunLoopSource bad CFMachPort, %s\n
Hand
LatencyServiceOpen
Kext identifier->path cache - kext info is not an array.
Link Training Command
ProximityWake
Hibernate Free Ratio
(invalid)
 for:
Stop
YCbCr 4:2:2 (HDMI tunneling)
Disk Sleep Timer
plugin
/System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
UTF32 Little Endian
assertion failure: Set report block already set
/usr/appleinternal/lib/HIDPlugins/ConnectionPlugins
IONotificationPortSetImportanceReceiver
Hibernate File
scheduledby
Audio
Value
Kext identifier->cache for %s - cache version missing/invalid.
OSBundleDependencies
HIDPreferencesCopy
IODPHDMIControllerPort
Personality CFBundleIdentifier names a kext that doesn't declare an executable
; reinitializing all kexts for new architecture
Split:         %s\n
HIDPreferencesSetMultiple
Cache file %@ is out of date; not using.
Personality %@ not found in %s.
Process must be running as root to load kexts.
Mkext length field %d does not match mkext actual size %d.
MaintenanceImmediate
HIDObjectUUID
IODeviceTree:/product
MatchingEvent
Timestamp
W:
Compatible version must be lower than current version.
Can't create kext cache under %s - owner not root.
Can't get info dictionary for %s.
PSR:           %s\n
Kernel error handling kext request - %s.
Close
EnergyMode
!hid_pthread_attr_init(&attribute, kIOHIDInterruptThreadPriority, kIOHIDInterruptThreadPolicy)
Front Left High
---------------------------\n
data
bootstrap_look_up2 failed with 0x%x\n
PrimaryUsage
AID
client
%s.%06d
Range:
Swipe
LatencyEventSystemOpen
UserKeyMapping
Class
Bad mkext magic/signature.
Transport:
/AppleInternal/Library/HIDPlugins/ServiceFilters
KeyboardLanguage
Source
HIDPreferencesCopyForInstance
Automatic
Standby Battery Threshold
filterEvent:toConnection:fromService:
ClearTime
workgroup_interval_force_enable
Traditional gamma (SDR)
Front Right Center
<%s %s>
Internal error; overrun mapping executable file %s.
DriverKit
Kext Request Lookup Address
ShipChargeLimitData
ShipChargeLimitEnabled
Button Mask:
IOHIDResource
%s, version %s is already in the identifier lookup dictionary at index %d.
SCDynamicStoreSetNotificationKeys
Failed to remove identifier->path cache %s - %s.
com.apple.iokit.iomigmachport
Invalid cache format %d specified.
HIDWaitCursorFrameInterval
assertion failure: Queue has already been activated/cancelled.
X:
IOKitLib.c
Automatic Restart On Power Connect
Changed
Kext declares no kernel/KPI libraries; if it references any kernel symbols, it may fail to link.
QueueState
%3lld%c 
time
<false/>
Watch
Personality has no CFBundleIdentifier; the kext's identifier will be inserted when sending to the IOCatalogue
Kexts already loaded for these libraries are not compatible with the requested version
DTS
Kext is not signed
zlib inflate discrepancy, uncompressed size != original size.
%s is a kernel component with no dependencies.
chargeSocLimitReason
Absolute
OSKextIdentifierCacheBasePath
Nameless (via IOPMAssertionCreate)
queueType
now
assertionAsyncOffloadDelay
DisplayWake
WillStopLink
Battery Power
XYZ
Stage:
Kext %s-space log filter changed from 0x%x to 0x%x.
KEXT
True
TimeoutActionRelease
USBDeviceCommand
Off
TCPKeepAlivePref
Details
Interfaces
&gt;
%@%@
YES
(date object)\n
Flushing info dictionaries for all kexts.
DCI-P3 (D65)
AutoPowerOff Enabled
CurrentState
CollectionCookie
IOHIDUserDevice
Range 
IOAVController
setBatteryDofu
RunLoop
assertionActivityUpdateOverflow
, DSC (%f bpp, passthrough)
/System/Library/PrivateFrameworks/HIDPreferences.framework/HIDPreferences
v12@?0C8
property
MultiAxisPointer
LastEventTime
virtualServices
propertyCacheMiss
Loading %s.
UnifiedSleepSliderPref
kern.waketime
HIDRMHash
OSBundleWiredSize
activityStateChangeCount
HIDMouseAcceleration
<integer>
18 Gbps (6Gbps/lane * 3 lanes)
{\n
dominoMainDisplay
IOHIDService name:%s id:0x%llx primaryUsagePage:0x%x primaryUsage:0x%x transport:%s locationID:%@ reportInterval:%d batchInterval:%d events:%d mask:0x%llx sensorcontrols:%d
DesktopModeAppliesOnBatteryPower
Pre-emphasis:  %d\n
PowerRelativeToShutdown
Dependencies have validation problems
Failed to send personalities to the kernel.
OSBundleRequiredPromotion
(unknown error)
/Library/Apple/System/Library/HIDPlugins
IOCFSerialize.c
syntax error
connection
IOParentMatch
Kext library %s using caches.
Standby Enabled
HighPowerMode
serviceNotification:added:
IOHIDValue
Architecture %s not found in mkext.
Link ID:      %u\n
returnCode
OSKextIdentifierCacheKextInfo
Can't serialize personalities for %s.
/Library/Apple/System/Library/HIDPlugins/SessionFilters
Test Mode:    %d\n
IOSystemStateNotification
com.apple.iokit.statenotification.name
/System/Library/PrivateFrameworks/TCC.framework/TCC
ClickCount:
%s/%s%@/%@%s%s%s
%s has multiply defined %ld symbol%s
TurnedOn
AppleLSIFusionFC
Rejecting invalid/inauthentic kext for bundle id %@ at location %@.
9 Gbps (3Gbps/lane * 3 lanes)
IsDeviceUsable
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n
Omitting loaded kext %s from mkext for kernel load.
Score
deviceID
PrepareLink
Internal
%s %d - cannot allocate memory for target string
IOHIDServiceFilter
NormalizedPositionDeltaX:
promotable 
CountryCode:
CalibrationSaturationMax
com.apple.kernel.6.0
Brightness
UTF16 Little Endian
CtrlKeyboardUsageMap
OSKext
_kasan
Front Center
(missing)
???
Kext identifier->path cache for %s - base path missing or invalid.
%s - loaded dependency %s, v%s is not compatible with requested version %s.
Pixel Clock:   %f Mhz (%u Hz)\n
%g kHz %dch %d-bit %s
Overscan
HeartRate
Monitor
Adding CFBundleIdentifier %s to %s personality %s.
ForceOffBusDisable
BT.2020 (RGB)
Orientation type:
0
Only incompatible kexts found for these libraries
assertionActiveAsyncByProcess
HDCP1
IdleSleepPreventersWithID
Flags:
Dependency lacks appropriate value for OSBundleRequired and may not be available during early boot
Can't create kext from cache: %s is already open and has a different CFBundleVersion from identifier->path cache entry %d.
dominoState
%-20.20s %dx\n
Driver Extensions may not use the %@ key; please remove.
Mkext checksum error.
state.setIDRefDictionary
IOCircularDataQueueCreateWithConnection
Can't load %s - ineligible during safe boot.
batteryKioskModeData
SLCheckInCapability
Start Exclude Level
com.apple.private.hid.client.event-filter.internal
BSD Name
/Library/Apple/System/Library/HIDPlugins/ServiceFilters
IODPController
SCDynamicStoreNotifyValue
%c[0m
FromEdgeFlat 
TargetBrightness:
B24@?0r*8^v16
Description
USB
CH3:
GTF
CoreGraphicsProgress
OSBundleRetainCount
.iohid
No Description
com.apple.iohidmanager
kernelEventQueue
/AppleInternal/Library/Extensions
The 'CFBundleIdentifierKernel' key is required in your personality to specify the base kext to load when your kext is instantiated.
Requesting start of %s.
/System/Library/DriverExtensions
Adding IOBundlePublisher %s to %s personality %s.
TimeoutAction
%s%s
PressCount
NoIdleSleepAssertion
Action
<%s ID=\"%d\">
SCPreferencesApplyChanges
queueHeaderShadow->allocMemSize == map_size
Manufacturer:
%-20.20s %s\n
 (dependencies not fully resolved) ->
assertionFeatureSupported
Channel %d: %s\n
:
IONameMatch
%02x%s
clientNotification:added:
UPSShutdownAtLevel
matching
com.apple.kext.unload
com.apple.PowerManagement
__LINKEDIT
filterSetProperty:forKey:forClient:
Unprotected
PID
UnprotectLink
Inactive
DispatchQueue
Properties
staticSize
 (with termnation of IOServices)
Master
Error initializing zlib uncompression for %s.
alloc
UUID
LongPress:
com.apple.iohideventsystem
assertion failure: Client has already been activated/cancelled.
Can't record kext in identifier lookup dictionary; no identifier.
IOAVDevice
scRGB
SleepServiceImmediate
lastNotifyTime
Kext logging %sabled for %s.
Opening %s for map.
%s - dependencies already resolved.
ProcessName
com.apple.private.hid.client.motion-event-privileged.internal
bg 
Z:
Quality:
tail
OSKextIdentifierCacheVersion
Finished reading identifier->path cache for %s.
com.apple.private.hid.client.admin
DST
_
Personality CFBundleIdentifier differs from containing kext's (not necessarily a mistake, but rarely done)
BatchInterval:
Audio Channel Layout
oflag
GetReportCnt
%s - dependency '%s' not found.
%s has no symtab in its executable (%s)
unknown
Architecture %s not found by CPU info (type %d, subtype %d), trying by name.
Cache file %@ - group not wheel; not using.
dis
Sending %d personalit%s to the kernel.
fd
Startup
False
IsPromoted
state.numberIDRefDictionary
Start 
matchConnection:
setEventDispatcher:
IOUSBDeviceDescription
string
,
assertionCreate
Calculated
Phase:
setProperty:forKey:client:
userDeviceQueue
Failed to read kexts requested by kernel since startup - %s.
Created mkext for architecture %s containing %u kexts.
9:14
HIDPointerButtonMode
Usage:
Cancel 
%s has no personalities to send to kernel.
%-20.20s True\n
InstanceMetadata
AudioChannelLayoutElements
CVT
DidUpdateMask:
PreventUserIdleSystemSleep
IOAVDisplayMemory
High Standby Delay
Built-In
Video Timing
IOHIDServiceConnectionCache
assertionUpdateActives
MaxChannelCount
HIDSessionFilter
GameController
momentum:
EstimatedPressure 
compatible 
AppleSmartBatteryManager
Validation Failures
Finished reading cache file %s.
SampleInterval:
PRBS7
AppleLSIFusionSAS
ICH8 ATA/100
Bluetooth
Accuracy:
Terminate IOServices
com.apple.system.powermanagement.useractivity2
Progress:
Some dependencies are causing circular references
%s found link dependency %s.
Trying to authenticate kext with no authentication function, failing.
DP
Irregularity:
Location:
 failed
ColorComponent0:
Direction Pad Left:
CountryCode
%s failed to compress executable.
ProductID:
Successfully loaded %s.
TimeoutTimeStamp
Bottom Button M3:
IOHIDService.c
Creating %s.
State
ClientEventFilter
Kext library setting simulated safe boot mode to %s.
%s is invalid; can't resolve dependencies.
HIDAnalyticsEventCancel
IOPower:/IOPowerConnection/IOPMrootDomain
adapterDetails
Scroll
AttributeDataLength:
procName
/System/Library/Caches/com.apple.kext.caches
URL = \"%@\", 
%s - internal overrun in executable file (%s).
com.apple.iokit.ioserviceauthorized
SleepWakeUUID
MajorRadius:
Shoulder Button R1:
DEXT
.hid
PolicyTimeoutTimeStamp
SCDynamicStoreCreateRunLoopSource
Can't create kext from cache: non-boolean OSKextEnableKextLogging in identifier cache entry %d.
f
Dolby TrueHD (MAT2.0)
idRef
Scale
Only Apple kexts may link against com.apple.kpi.private.
Interface kext must have exactly one dependency.
Error encountered, unmapping executable file %s (offset %lu, %lu bytes).
Reserved
com.apple.system.powersources.percent
Locked
Can't create kext: missing or non-string path in identifier cache entry %d.
w
MobileMotionModule
dispatchQueue
eventQueue
com.apple.userspace_ethernet
Dependencies aren't loadable during safe boot
Kext Request Info Keys
DeviceUsagePage:
AmbientLightSensor
HandTap
__IOHIDEventSystemRegister
Found %s.
EventFilterMask
Video Color
UTF32 Big Endian
caller
Kext identifier->path cache for %s - not a dictionary.
AAC
DarkWakeBackgroundTasks
com.apple.system.IOPMSchedulePowerEventNotification
...(%u bytes total)
FromEdgeTip 
/System/Library/Frameworks/Security.framework/Security
Releasing CFBundle for %s
PackID
Front Left Center
setProperty:forKey:
Kext has no executable or compatible version, so it should not declare any OSBundleLibraries.
Couldn't read resource URL in %s for resource %s.
UPSShutdownAfterMinutes
IOHIDManagerStateQueue
%-20.20s %s (%d)\n
*
Sending named personalities of %s to the kernel:
Face Button X:
HighFrequency
IOKitDebug
xvYCC601
resetCount
HandleReportCnt
IOHIDSystem
CH0:
.kext/
Mobile Motion Module
SCDynamicStoreAddWatchedKey
ies
MaxLinkRate
com.apple.
Performance_Warning
Memory allocation failure.
%s already has dependencies resolved.
ProtectedServicesDisabled
CH1:
CASecureLayerOnScreen
GlobalUniqueID
assertion failure: Device has already been activated/cancelled.
%s:%@
IOHIDEventSystemClientIsUnresponsive
Temp cache file name too long: %s.
YCbCr 4:2:2 (DP tunneling)
BT.709
ActivityTimeout
IOHIDConnection process:%@ pid:%d uuid:%@ caller:%@
PowerNap
%s:%s%s%s%s%s%s%s
SCDynamicStoreCreate
IOAccessoryHSAIDBulkData
keeping
IsCoalesced
Front Left
SwipeLeft 
%s: %s - no such file or directory.
DidStartLink
v12@?0I8
IOAccessoryIDBusBulkDataEndpoint
IOHIDQueue
TouchSensitiveButton
Color Attributes:\n
<%s>
Button
Can't stat %s - %s.
OSBundleUUID
Can't determine real path for %s (%s)
assertionActivityUpdateRefCnt
DestroyFVKeyOnStandby
wake
SLCheckIn
File access failure; can't open, or I/O error
/AppleInternal/Library/HIDPlugins/ServicePlugins
5:4
chargeSocLimitNoChargeToFull
Extra Button R4:
mkext data
Can't load %s - dependencies ineligible during safe boot.
Warnings
PrimaryUsage:
SystemSleepPreventers
Resolving dependencies for %s.
IOHIDManager
userActivityRegister
Twist:
Failed to create kext request.
LastActivityTimestamp
Can't rename temp cache file to %s - %s.
Mkext plist has no kexts.
AutoTimesout
%-20.20s %ld\n
SecTaskGetCodeSignStatus
Length
OSKextVariantOverride
Lane %d:\n\n
Hot Plug
Rear Left Center
RequestTerminate
SCPreferencesCommitChanges
AppleLSIFusionSCSI
&amp;
batteryShippingChargeLimitAction
/System/Library/Extensions
assertionId
PowerByCalendarDate
SessionFilterDebug
The kext contains a symlink which is either not readable or points outside of its bundle; please remove
DolbyVision LL YCbCr 4:2:2 (HDMI tunneling)
batteryGaugingMitigation
serviceplugin
IOHIDEventSystemClient
AppleSecurityExtension
Wake On Modem Ring
StageProgress:
%s is not valid.
description
ForcePending 
GestureType:
runloop
EventType
assertionUpdateActivity
buttonState: %ld
%-20.20s 0x%016llX\n
Kext identifier->path cache for %s - kext entry not a dictionary.
HIDPreferencesSetDomainForInstance
__IOHIDEventSystemClientRefresh
SetReportCallback
 %@=%d
boolean, <true/> or <false/>
Failed to read XML from mkext: %s.
filterEvent:forClient:
%F %H:%M:%S
assertion failure: Manager has already been activated/cancelled.
Symlink points outside of bundle.
DolbyVision VSVDB
NXSystemInfo
qos
com.apple.kpi.kcov
zlib deflateInit failed.
Total Latency:
Relative
Add Child
%s not found in identifier lookup dictionary%s.
DefaultConfiguration
WMAPro
sYCC601
IOCFUnserialize: can't alloc temp memory
Standby Delay
eventtype
PM Notifications
DockSwipe
IOHIDEventSystem.c
Product:
ActivityTime
DoCFSerialize
Encoding:
com.apple.hid.analytics.service
Failed to serialize kext request.
256:135
Gyro
Position 
Cache file %@ - owner not root; not using.
loaded 
EventFilteredCount
Audio Stream Data:\n
16:10
ColorSpace:
Passthrough-only
Transport Type
v12@?0i8
LongPress
Kext library recording diagnostics%s%s%s%s%s.
Kext Request Arguments
Unregistered
Power Management power source queue
String/URL conversion failure.
 not
category < kIOHIDLogCategoryCount
Direction Pad Up:
Internal error, invalid argument to __OSKextCheckURL.
Loaded kext info:\n%s
LastDroppedEventTime
com.apple.system.accpowersources.source
BrightnessChanged:
Mapped executable file %s (offset %lu, %lu bytes).
AssertionOnBehalfOfPID
PortNumber
ATRAC
0x%qx
PowerOnImmediate
Serial
Motion:
Shoulder Button L1:
GRGB Tunneled as YCbCr422 (Even line blue)
CP2520 Pattern 1
status
chargeSocLimitIsEOC
IOHIDEventSystemClient State
com.apple.iohideventsystem.available
active
Dependencies have incorrect owner/permissions
Reading resource file %s%s.
ActivityState
object
Cancelled
AngleDegrees:
Authenticating %s file/directory %s.
/System/Library/AppleUSBDevice/USBDeviceConfiguration.plist
ConfigurationType
services
Reading cache file %s.
assertions
System Sleep Timer
HIDClickTime
_MKEXTExecutableRelativePath
filterEventMatching:event:forClient:
MinLaneCount
AppleUSBXHCI
Automatic Restart On Power Loss
IsPowerOn
displayUUID
 warnings
Set Power
setCancelHandler:
TCCService
assertionUpdateCategoryPolicy
9:15
BT.2020 (YCbCr)
IOAVVideoColorBitsPerPixel
IOHIDDevice
initWithSession:
 authentication
Orientation
SwipePending 
Note: OSKextCopyKextsWithIdentifiers() - identifier %s not found.
Negotiating
vendorUsagePage: %ld vendorUsage:%ld dataLength:%ld
Third-party Driver Extensions are ineligible to run in Safe Boot, or match on devices during early boot. Please remove the OSBundleRequired key from your Info.plist.
MaxState
Failed to open compression stream for %s - %s.
DeviceUsage:
manufacturerString
poweron
SCPreferencesCreate
version
DroppedEventCount
UsagePage
Right Headphone
hideventsystemclient.default.queue
Flushing load info for all kexts (%s dependencies)
Failed to read contents of %s, CFURL error %d.
IODPService
SerialNumber
Category
Kext isn't loadable during safe boot.
Rotation
64-bit kexts must use com.apple.kpi.* libraries, not com.apple.kernel* libraries.
SupportsDownspread
1:1
IOCFUnserializeBinary
IORegistryEntryID
IOAVControlInterface
IOAccessoryIDBusBulkData
ServiceFilterDebug
Delay Autounload
GPUSwitch
ReduceBrightness
%-20.20s 
Kext is a kernel component but OSBundleIsInterface is set to false; overriding
size=\"%d\"
com.apple.kernel.
BundlePath
%dx%d%c %.3f Hz, %dbpc %s Range %s, %s colorimetry, %s EOTF
GRGB Tunneled as YCbCr422 (Even line red)
MaxInputReportSize
 (dependencies not resolved).
default
: 
Continuous
Sticky Key Phase:
GetReportCallback
ResourcesUsed
Layout:\n
state.stringIDRefDictionary
UserActivityLevels
.plist.gz
Start Matching Exclude Level
Can't load %s - dependency authentication problems.
%s (version %s%s%s): same version, different UUID (%s) is loaded.
Link Command (with source)
HIDConnectionPlugin
HIDInterfaceID
vid 
devices
0x0
plist
SwipeDown 
%-25.25s %d\n
Failed to close compression stream for %s - %s.
WakeDisplay
ColorComponent1:
v24@?0^v8^v16
copyEvent:matching:options:
Can't load %s - validation problems.
AppleSmartBattery
Open failed for %s - %s.
AssertPID
SCDynamicStoreCopyValue
%@#%@
Searching for link dependencies of %s.
DeviceUsagePairs:
SetDeviceDescription
MPEG1
<%s ID=\"%d\" %s>
HIDKind
Directories
IOCFSerializeBinary
Unit
assertionTimeout
PreciseAspectRatio
+
sentinel %qx\n
Boot Level Restrictions
SetPower
Front Left Wide
wakepoweron
Product
NextThreshold:
Couldn't open CFBundle for %s.
Requests from kernel missing or of wrong type.
!parent
NavigationSwipe
assertion failure: CFMachPortCreateWithPort
CFBundlePackageType is DEXT and bundle declares CFBundleExecutable; use only one.
_MKEXTInfoDictionaries
SleepDisabled
SwipeRight 
Thumbstick Button Right:
NormalizedPositionX:
Statting %s for map.
score
ReleasedThreshold:
InterfaceRole
Authentication Failures
Reading resource %s.
Reading load info for all kexts.
AppleKernelExternalComponent
com.apple.powermanagement.collectbt
Minor
UsagePage:
AuxiliaryPressure:
Ungroup for legacy clients
IOHIDEventSystemClientDispatchMach
Failed to open CFBundle (unknown error).
/System/Library/HIDPlugins/ConnectionPlugins
IsVirtual
Video
ButtonMask:
options
IOAppPowerStateInterest
usagePage: %ld usage: %ld children: %ld ungroupForLegacy: %ld
Down:
Failed to open CFBundle for %s.
LocationID:
HIDAnalyticsEventCreate
SMPTE 170M/BT.601
Carrier Mode
Stylus
Kext Request Predicate
Failed to read loaded kext info from kernel - %s.
DTSHD
batteryChargingIconoGraphy
Not running as root; skipping save of identifier->path cache.
com.apple.kernel
Can't load %s - a different %s is already loaded.
Released
Established
<off> 
Can't create kext cache under %s - group not wheel.
__unknown__
<data>
Executable kext %s with no dependencies?!
None
HIDPreferencesSynchronizeForInstance
Architecture %s not found by name, using running kernel architecture %s.
Stat failed for %s - %s.
Rear Right
Carrier Mode Low Voltage
IOPSPrivateBatteryHealthState
Services
Phase
assertionCheckCount
AttributeData:
TransducerType:
Info dictionary missing required property/value
Can't load %s - no code for running kernel's architecture.
/usr/appleinternal/lib/HIDPlugins/ServicePlugins
%u
none
LiftOffPredicted 
Can't read running kernel architecture.
.XXXXXX
ID = \"%@\"
, DSC (%f bpp, decompress)
Front Right
Density:
__OSKextCreateKextsFromURL
StopLink
IOProviderClass
ChildEvents:
Face Button A:
ServiceRecord
Kernel load info for %s lacks a CFBundleVersion.
EnableIdleSleep
IOCircularQueueDescription
)\n
trace
Resting 
initWithConnection:
LocationID
%s has no info dictionary; can't resolve dependencies.
/System/Library/HIDPlugins/SessionFilters
failed to open io_service_t err=0x%x
Location
IOAVService
SetDevicePreferredConfiguration
%-20.20s %s%s\n
14:9
HIDCapsLockLED
kr == KERN_SUCCESS
HIDAnalyticsEventSetStringValueForField
cpu 
%s found %s%s%sdependency %s for %s%s.
%x, %lx, 0x%llx, 0x%llx\n
Kext has a CFBundleExecutable property but the executable can't be found
HIDPreferencesCopyMultipleForInstance
Thermal_Level_Warning
Kexts may not use the DriverKit value for OSBundleRequired.
com.apple.private.hid.client.admin.internal
Cache file %@ - wrong permissions (%#o, should be %#o); not using.
External
HDCP
/
Unknown
IOHIDDeviceSuspend
ClickSpeed:
PrimaryUsagePage:
Sender
 }
.DS_Store
/usr/appleinternal/lib/HIDPlugins/ServiceFilters
Product Description
Transition: Exit
Can't load %s - dependencies ineligible during safe boot:\n%@
%s (version %s): is%s started.
</key>
Connections
kernel
user
HIDActivityState
MinorRadius:
Can't load %s - authentication problems.
AssertLevel
pid
deviceProtocol
<key>
SwipeUp 
&lt;
IONetworkInterfaceProperties
SleepFailure
Dispatch Latency:
%-20.20s %08x\n
IOMIGMachPort
Sending all personalties for %s to the kernel.
RestartInterfaces
\n
DataLength:
ended
Symbol Error Rate Measurement Pattern
TCCAccessPreflight
SCPreferencesCreateWithAuthorization
Attempt to set 64-bit load address - %s.
For loaded kext %s, v%s: no opened kext matches.
VendorID:
com.apple.private.hid.client.service-protected
deviceSubClass
LinearPCM
yes
Creating kexts from identifier->path cache for %s.
Error uncompressing kext cache file %s - zlib returned %d - %s.
Audio Channel Layout Data:\n\n
HIDPreferencesCreateInstance
Rz:
ClickDownPredicted 
filterEvent:
Failed to load %s - %s.
HIDAnalyticsEventAddHistogramField
internal error
createOptions
Kext was not created from an URL and can't be authenticated
 validation
%s is already open; returning existing object.
%s Element\n
state.arrayIDRefDictionary
batteryGaugingMitigationState
_IOHIDLogCategory
tcc_authorization_check_audit_token
Key
IOUserEthernetInterfaceMergeProperties
ColorModes
IOKitPersonalities
Kexts should declare dependencies on either com.apple.kernel* or com.apple.kpi.* libraries, not both.
Failed to check path %s (CF error %ld).
Dolby TrueHD (MAT2.1)
Rear Right Center
Front Center High
Selectable
array
%@#%04lx#%04lx#%016lx#%ld
%s.IOHIDQueueRef
Reduce Processor Speed
DesktopMode
ForceStage
LastActivityTime
lastNotifyEventTimeStamp
DolbyVision (native)
Limited
BT.2100 HLG
Bottom Button M2:
Transition: None
%s: %s\n
LegacyBatteryInfo
UPSDefaultThresholds
com.apple.powermanagement.sleepservices
SCError
LatencyCopyEvent
MP3
Kexts with a kernel library < v6.0 must set MODULE_NAME the same as CFBundleIdentifier to load on kernel < v6.0.
VFTG
FIXME: IOUnserialize has detected a string that is not valid UTF-8, \"%s\".
Left Headphone
LogLevel
Personality Names
Unload
/System/Library/HIDPlugins
VESA
EventType:
Sticky Key Toggle:
OSBundleRequired not set
%s
%s added %u-byte %scompressed executable to mkext.
Caller
com.apple.iokit.powerdxpc
Sleep
IOHIDManager State
Number:
Clearing \"has all dependencies\" for %s.
Failed to uncompress %s%s from %s.
IOSleepSupported
_kTCCAccessRequestOptionSyncCallback
Bottom Button M1:
zlib inflateInit failed.
StartLink
Command
UPSShutdownAtMinutesLeft
Probability:
v48@?0^v8^v16^v24^v32^v40
Internal error converting URL
MaxPropertyNotificationHandlingTime
assertionActivityUpdateProcessList
sizeof(IOCircularDataQueueDescription) == inband_outputCnt
Closed
IOServicePublish
OSKEXT_BUILD_DATE 16:20:56 Oct  3 2026
, no UUID
FullWake
Unable to get data to create cache file %s.
Failed to get %s for portType=%d, portNumber=%d, portVariant=%d\n
invalid pixel encoding
IOCircularDataQueueImplementation.h
HandTapHold
IOHIDUserDeviceStateQueue
<IOHIDUserDeviceRef ref:%d/%d id:0x%llx stats:%d,%d,%d>
OSKernelCPUSubtype
Front Right Wide
Personality CFBundleIdentifier names a kext that is not loadable (run kextutil(8) on it with -nt for more information)
OSBundleUsesAbsolutePath
%s adding implicit KASan dependency
PrioritizeNetworkReachabilityOverSleep
SCDynamicStoreSetValue
Progress
Compass
hid-workgroup-interval
Reading list of all kexts requested by kernel since startup.
Failed to parse kernel log messages: %s.
Can't load %s - failed to resolve dependencies.
<dict>
IOHIDSession - SessionEventDispatch
Could not get absolute path of kext!
Can't open CFBundle for %s.
Kext personality for kext %s is not a dictionary
%s (version %s%s%s) is loaded.
%@:
TimingStandard
Intermediate
Wake On Clamshell Open
ups
allocator
IOHIDEventSystemClient.c
%s:\n
AutoPowerOff
com.apple.system.powersources.source
com.apple.private.hid.client.event-dispatch
DolbyVision LL RGB 4:4:4
0 Gbps (FRL disabled)
Bottom Button M4:
-----------------------------------------------------------------------\n
!pthread_create(&__serviceRunLoop.thread, &attribute,(ThreadRoutine)&__IOHIDServiceRunLoopCompatibilityThread, NULL)
Total Channels: %d Active Channels: %d\n
v16@?0^v8
name
EventMask:
NormalizedForceVelocity:
SCPreferencesGetValue
Failed to serialize data for cache %s.
%s adding implicit Kcov dependency
type
PrimaryUsagePage
Tap
CPU_Power_Limits
Removing identifier->path cache %s.
unknown CPU architecture
CFBundleIdentifierKernel
%s has no Info.plist file.
10:16
IOPMSleepFailure
hidsignpost
UNKNOWN
Can't open cache file %s, CF error %d.
Link Training Data:\n\n
Downstream
Shake
com.apple.hid.analytics.event-system
VersionNumber
OSBundleStarted
/Library/Apple/System/Library/Extensions
OneBitAudio
SCDynamicStoreKeyCreatePreferences
StandardType
4:3
service
_IOPMCreatePowerOnDictionary received invalid date\n
VendorIDSource
HIDIdleTimeMicroseconds
OS
IOHIDActivityUserIdle
keyboardPress: %ld
_%s
Swing Voltage: %d\n
SCPreferencesUnlock
Translation
DoubleSqueeze
NormalizedForce:
Failed to get file info (stat failed)
Interlaced:    %s\n
NO
IdleSleepPreventers
IOAccessoryBulkDataEndpoint
Horizontal
PowerSource
CH2:
Normal
IOHIDEvent Server Connection - Root
Compressed executable from %u to %u bytes (%.2f%%).
Dolby Atmos (MAT2.0)
YCbCr 4:4:4
Proximity
com.apple.powerd.assertionoffloadtimer
Full
40 Gbps (10Gbps/lane * 4 lanes)
IsLowPower
Thumbstick Button Left:
 (kernel component)
_kmod_info
Mkext plist full size is %u.
assertionActivityUpdateData
/IOKit/PowerManagement/SystemLoad/Detailed
%s not in base path %s for identifier->path cache - marking.
zlib inflate failed: %s.
The booter does not recognize symbolic links; confirm these files/directories aren't needed for startup
original URL = \"%@\", 
MinLinkRate
v24@?0Q8Q16
Biometric
Tap Count:
 off
135:256
com.apple.iokit.IOServiceAuthorizeAgent
ActivityLog
IOHIDEventSystemConnection uuid:%@ pid:%d process:%@ type:%s entitlements:0x%x caller:%@ attributes:%@ state:0x%x events:%d mask:0x%llx dropped:%d dropStatus:%d droppedMask:0x%llx lastDroppedTime:%@
HandFlick
Transport
Peak 
AsyncRemoteAssertionId
Audio Link Data:\n
uniqueDeviceID
userdevice
Path
Shoulder Button R2:
Realizing %s from identifier cache object.
Can't create %s - %s.
UserVisible
IOKit Power
Queue
Failed to remove personalities of %s from IOCatalogue - %s.
Found plugin %s.
Can't get executable for %s (architecture %s).
ProtectLink
Can't create kext: missing or non-string CFBundleIdentifier in identifier cache entry %d.
Lane Count:    %d\n
HIDCapsLockState
Deprecated property (ignored)
YCbCr 4:2:2
DMT
Started %s.
HIDPreferencesSetForInstance
AppleClamshellState
File not found
Requesting unload of %s%s.
filterEvent:forService:
%-20.20s 0x%016llx\n
AC3
15:9
state.dataIDRefDictionary
batteryChargingIconoGraphyAction
_IOHIDServiceCreate_block_invoke
ProbeScore
Mkext plist compressed size is %u.
TimeoutSeconds
Auto
eventMask
%s%s (%s)%s
DownstreamFormat
Link Command
State:
/IOKit/Power
 ->
Failed to stop %s - %s.
Compressed info dict from %u to %u bytes (%.2f%%).
Mask:
Attribute 
ColorComponent2:
IOHIDNotification
IOClassNameOverride
CalibrationMax
PressCount:
Info dictionary property value is illegal
Couldn't read resource file %s.
ForceOffBusEnable
integer
Kext personality %s subentry is not a dictionary
IODPDevice
PortVariant
batteryCycleCountData
SampleInterval
Reading requests from kernel.
%s - Interface kext must have exactly one dependency.
Can't read info dictionary for %s: %s.
(\n
Usage
SubType:
Version:
HID - IOService Enumeration
Rate Controlled
HIDDebug
CFBundleIdentifier and CFBundleVersion must be < 64 characters.
executable
RetrainLink
cancel
ConfigurationDescriptors
80-bit custom pattern
IOHIDSessionFilterRef uuid:%@ name:%@ %@
UTF8
velocityDegreesPerSecond:
droppedEvents
Failed to set permissions for %s - %s.
com.apple.kpi.dsep
com.apple.iokit.statenotification.create
Hibernate Mode
Wake On AC Change
%s has %d remaining undefined symbol%s
OSBundleIsInterface
6.0
%s: 
Rear Center
getTagString
IOPMPowerSource
Transition: Enter
Flushing dependencies for %s.
Kext Request Result Code
OSKernelResource
%s - missing load info or dependencies array in applier function.
shutdown
%-20.20s %llu\n
Extended
(unknown)
Dolby Atmos (MAT2.1)
StreamSampleRate
PropertyNotificationCount
Other
IOHIDQueueDispatchMach
USBDeviceCommandParameter
[^/]+
DroppedEventMask
identity
FluidTouchGesture
NSPrincipalClass
%s.IOHIDDeviceRef:0x%llx
HIDDefaultSensorControlOptions
Saving cache file %s.
Requesting stop of %s.
<integer> (kexts may not use <real>)
com.apple.private.hid.client.debug-tool
CapsLockDelayOverride
gamingEnergyMode
Failed to remove temp cache file %s - %s.
Root
DeviceDescription
 %@=%@
MaxEventLatency
assertion failure: IODataQueueAllocateNotificationPort
Kext declares both CFBundleExecutable and CFBundleSharedExecutableIdentifier; use only one.
Unknown CPU info given (type %d, subtype %d), using running kernel architecture %s.
Kext library architecture set to %s%s.
Can't create kext: invalid CFBundleVersion in identifier cache entry entry %d.
Began
IOKit Power Source Copy
Direction Pad Right:
PropertyCache
Checking CFBundle of %s for executable URL.
Flushing dependencies for all kexts.
SenderID:
com.apple.iokit
AVI
Hibernation
com.apple.system.powersources.timeremaining
batteryShippingChargeLimitState
IOPropertyMatch
'%@' -> '%@'
kTCCServiceListenEvent
IODeviceTree
Up
Depth: [%d bpc] Encoding: [%s] Range: [%s] Colorimetry: [%s] EOTF: [%s] DSC: [%s]\n
CP2520 Pattern 2
WakeOnMagicPacket
b
EstimatedAltitude 
Can't create kext: path in identifier cache entry %d doesn't name a kext.
OSBundleCompatibleVersion
assertionSetState
MaxPower
DolbyVision LL YCbCr 4:4:4
state.dictionaryIDRefDictionary
TCCAccessRequest
QueueCallbackTimestamp
IOCFUnserialize: %s near line %d
IOGeneralInterest
EAC3
Upstream
 (from mkext)
Kexts already loaded for these libraries have no OSBundleCompatibleVersion
_MKEXTBundlePath
HIDMouseScrollAcceleration
assertionInitialConnection
Force
Multiple kexts for these libraries occur in the dependency graph
Console
/AppleInternal/Library/HIDPlugins/SessionFilters
%s:\n\n
Open
Realpath for %s is %s
%02x 
Failed to read requests from kernel - %s.
incompatible 
ReportInterval:
Video Link Data:\n\n
state.data
IODeviceTree:
batteryChargingIconoGraphyState
DarkWake
EstimatedAzimuth 
Filters
ThermalWarning
GenericGesture
not
Removed %s, id %s%s, version %s.
<string>
Invalid
Administrative
unknown error
IOProbeScore
FrameworkBundleID
LowSNRSwipe 
claimSystemWakeEvent
SCPreferencesLock
Events:
Unsupported mkext version 0x%x.
Front Right High
IOUSBHostDevice
IOHIDEventSystemClientNotifyDispatchMach
Extracting %s%s from %s.
IOServiceFirstMatch
mkext URL = \"%@\", 
assertionCheck
fastpath
IOHIDEventQueue
DSCRequiredColorElementIDs
Start
Validating %s.
Load
IOPathMatch
Can't create kext: missing or non-string bundle package type in identifier cache entry %d.
setting load address of %s to 0x%0x
AspectRatio
16:9
HIDKeyRepeat
PowerManagement
v28@?0Q8^{dispatch_mach_msg_s=}16i24
Keyboard
GenerationCount:
HIDPointerAccelerationType
AdobeYCC601
id
activity
v24@?0r^v8r^v16
HDMI
SystemPowerProfileOverrideDict
%-20.20s %u\n
Generation:
IO
TimeoutActionTurnOff
com.apple.iohidmanager.uuid
HIDResetPointer
<
%s\n
Flushing info dictionary for %s.
AssertionOnBehalfOfBundleID
HIDAnalyticsEventActivate
chargeSocLimitToken
<IOHIDEventSystem %p [%p]>{\n\tserviceDict=%@ \n\tnotificationDict=%@ \n\tmatchNotifySet=%@ \n\tclientSet=%@}
PortType
DSC:          YES (%f bpp, passthrough)\n
push 
0x%llx
%s: internal overrun in executable file (%s).
HIDScrollAcceleration
Manufacturer
<IOHIDNotificationRef %p (ref:%d xref:%d), flags:%x  %p,%p,%p,%p,%p,%p>
 dependencies
Reading load info for %u kext%s.
Failed to create lookup address object.
%s - dependency for %s lacks valid OSBundleCompatibleVersion.
Remove Child
Kexts with a kernel library < v6.0 must set MODULE_VERSION the same as CFBundleVersion to load on kernel < v6.0.
%-20.20s ERROR\n
IOUSBDeviceDescription: pid/vid/ver=%04x/%04x/%d class/sub/prot=%d/%d/%d Mfg:%@ Prod:%@ Ser:%@\n%@
64:27
0x%lx
DPCP
%s does not declare a kernel dependency; using %s.
Capture
DisplayDims
%@#%@#%@#%@#%@
MotionGesture
CEAShortID
serialNumber
SCPreferencesSetValue
Name
%-20.20s %f\n
LatencyDispatchEvent
(data object)\n
IOUSBHostInterface
IOHIDTransaction
assertion failure: Get report block already set
Failed to unload %s - %s.
Virtual:
TimedOut
deviceClass
OSBundlePrelinked
ElementData
Detailed
? Gbps (Unknown FRL rate)
</%s>
ForceActive 
MayBegin
%s, version %s recorded at index %d in the identifier lookup dictionary.
%s does not contain code for architecture %s.
AssertType
/usr/appleinternal/lib/HIDPlugins
ElementType
unexpected end of buffer
activate
Confidence:
Can't create kext: missing or non-string version in identifier cache entry %d.
HIDPreferencesSetDomain
ProximityDarkWake
SwipeLocked 
com.apple.private.hid.client.event-monitor.internal
Fast:          %s\n
productID
HIDPointerAcceleration
port
batteryShippingChargeLimitEnable
IOHIDLibPrivate.c
kern_result == KERN_SUCCESS
Get Kernel Requests
Enhanced Mode: %s\n
HIDServiceAccessEntitlement
Kexts found for these libraries lack valid OSBundleCompatibleVersion
com.apple.kpi.kasan
LogIOHIDFilteredEvents
OSBundlePath
assertionWasCoalesced
Ethernet
TransducerIndex:
Low Frequency Effects
```
