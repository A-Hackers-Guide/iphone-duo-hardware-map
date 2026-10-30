# `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`

iOS 27.2 dyld shared cache image. Version `100288.40.8.0.1`. **[DSC]**

## Linked libraries (6)

- `/usr/lib/libenergytrace.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/usr/lib/libz.1.dylib`
- `/usr/lib/libbsm.0.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/usr/lib/libobjc.A.dylib`

## Objective-C: 7 classes, 0 protocols, 22 methods, 0 properties

### Class pages

Every class and protocol, with its methods: [`HIDConnection`](../objc/HIDConnection_IOKit.md), [`HIDDevice`](../objc/HIDDevice_IOKit.md), [`HIDElement`](../objc/HIDElement_IOKit.md), [`HIDEvent`](../objc/HIDEvent_IOKit.md), [`HIDEventService`](../objc/HIDEventService_IOKit.md), [`HIDServiceClient`](../objc/HIDServiceClient_IOKit.md), [`HIDSession`](../objc/HIDSession_IOKit.md)

### Classes

`HIDConnection`, `HIDDevice`, `HIDElement`, `HIDEvent`, `HIDEventService`, `HIDServiceClient`, `HIDSession`

## Strings (2,602)

```
IORegistryEntrySetCFProperty Failed for kIOHIDActivityUserIdleKey with err : 0x%x
IOPMUnregisterNotification: no valid ref for 0x%lx
Connection removed: %{public}@
CopyServiceRecords deep copy failed. Service record for %@ is not serializable.
%s: %@ is missing the '%s' entitlement
io_hideventsystem_create_virtual_service :%x
io_hideventsystem_dispatch_event_for_virtual_service:%x
assertion failure: \"pthread_mutex_lock(&(queueContext)->lock)\" -> %llu
Service:0x%llx  is unregistered, not matching
Event filtered type:%d sender:0x%llx eventInfo:(%@) service filter:%@
IOPMAssertionCreateWithProperties: One of the arguments is NULL
Received connection invalid error for connection 0x%lx. UnregisterNotification
Unable to create queue analytics
Sending assertion create msg for id 0x%x:%@\n
Setting Assertion State for PID %d to %d\n
Replying to assertion check message with count %d token:%llu\n
IOHIDEventSystemServiceRemove
assertion failure: \"pthread_mutex_lock(&(service->queueContext)->lock)\" -> %llu
Failed to find %s for synchronize, switch to default CFPreferences
probe failed for plugin for %@
Received an error in response to copy scheduled wake data\n
IOHIDEventSystem - enumeration queue termination
0x%llx: IOServiceAddInterestNotification 0x%x
%s: mach_port_deallocate(reply_port):%s
%s: mach_port_deallocate(oldNotify):%s
Re-syncing assertions
Setting async client assertion id to 0x%x
onePlugin invalid for pluginType %@
IOHIDSessionCreate - Load bundles
Invalid ReportInterval: %@
Invalid BatchInterval: %@
%s
QueryInterface(kIOHIDDeviceDeviceInterfaceID):0x%x
assertion failure: \"__IOHIDQueueSetupAsyncSupport(queue)\" -> %llu
%s: iohideventsystem_client_dispatch_notification_results:0x%x
No assertions by process
Received an error in response to copy assertion activity
Set cursor bounds minx:%d miny:%d maxx:%d maxy:%d
Loading session filter:%@
Timeout is less than 0 %d
PowerD error: 0x%x\n
IOHIDConnectionFilterCreate Failed to initialize plugin
0x%llx: IOHIDService property %s incorrect type: %@
0x%llx: IOHIDUserDevice start failed:0x%x properties:%@
unregisterNotification: invalid ref to 0x%lx
Failed to create IOPMConnection. rc:0x%x\n
IOHIDEventSystemAddService
Unable to allocate client reply port
Successfully opened the IOHIDSession
assertion failure: Cancel failed queue: %p runLoop: %p
%s: HIDVS ID:%llx iohideventsystem_client_dispatch_virtual_service_notification:%x
Update assertion policy %llu
_releaseAsyncAssertion: Failed to get the assertion details for id:0x%x\n
Failed to create event at index=%d eventCount=%d eventDataOffset=%d lenght=%ld
%@
restore property %@ to %@
%s: mach_port_deallocate(notifyPort):%s
there is a timeout for category %@ and policy %@
Assertion has a category %@
Assertion 0x%x not found to activate
Failed to register for server availability: %d
[%#llx] Invalid entitlements property, expected Array or String
IOHIDServiceFilterFilterSetPropertyForClient %@  %@ -> %@ filter:%@
Set on screen cursor bounds px:%d py:%d minx:%d miny:%d maxx:%d maxy:%d
Failed to create PM queue\n
Service: %@ trigger matching failed: service is already registered
%s: iohideventsystem_client_dispatch_client_records_changed:0x%x
Service plugin %@: %@ never called cancel handler for service: %@
0x%llx: unresponsive:%@ client:%@
%s: HIDVS ID:%llx Invalid parameters: key:%@
Creating deep copy of record belonging to service: %@
Failed to convert CF dictionary to xpc object\n
processAssertionUpdateActivity unread-count %d
handleAssertionLevel for 0x%x to %d: %@
Could not find TCC symbol \"TCCAccessPreflight\"
HIDVS (id: %llx) does not exist
0x%llx: unschedule from dispatch queue completed
processCurrentActiveAssertions: No gAssertionConnection
Insufficient permissions to set kIOHIDSessionCASecureLayerOnScreenKey for UUID: %@
Failed to create CF properties: 0x%x\n
All actions on server queue completed.
0x%llx: os_workgroup_interval_finish(cancel) error: %d, service %@
%s: mach_msg(sendPossiblePort):%s
IOObjectRetain:0x%x
assertion failure: Schedule failed queue: %p runLoop: %p
Failed to create ASBM services\n
Bad matching event
HIDVS (id:%llx) does not exist
assertion failure: \"pthread_mutex_unlock(&(service->queueContext)->lock)\" -> %llu
__IOHIDServiceLoadObjcServicePlugin plugin did not provide passive matching dictionary %@
%s: Connection filter added:%@
assertion failure: \"completionElement\" -> %llu
%s: Event latency:%lld type:%d sender:0x%llx
%s: mach_port_request_notification(notify) unexpected old notify port %#x
%s: Sent client refresh msg, status:%#x
assertion failure: Failed to get queue port %p %p
__IOHIDServiceLoadServiceFilterBundles failed to find symbol %@ for bundle %@
%s: Event enqueue error:0x%08x type:%d sender:0x%llx
Received a release not for gCurrentRemoteAssertion:0x%x. Received 0x%x
IOHIDEventSystem - service queue termination
0x%llx _IOHIDServiceCreate failed to load service plugin ret: 0x%x score: %d objcScore: %d
IOHIDServiceFilter cancel handler invoked more than once for filter:%@
Failed to register for reconnect with powerd 0x%x
Failed to create xpc reply object
Loaded %ld HID plugins (%@) %@
No category
Released assertion id gCurrentRemoteAssertion: 0x%x: 0x%x.Logging everything to powerd %@ %ld
IOHIDSessionCreate
Can not locate kernel service
Failed to find %s for set, switch to default CFPreferences
Failed to create xpc connection
__IOHIDServiceCreateObjcServicePlugin class does not conform to HIDServicePlugin protocol
io_service_t has no plugin for %@
0x%llx: os_workgroup_interval_start error: %d, service %@
Copy Event filtered type:%d sender:0x%llx eventInfo:(%@) service filter:%@
Could not find TCC symbol \"TCCAccessRequest\"
Could not find TCC symbol \"TCCAccessCheckAuditToken\"
failed to get interface for plugin for %@
Service filter %@ never called cancel handler for service %@
IOHIDServiceFilterCreateWithClass Failed to initialize filter
%s: Unable to create activity timer
%s: HIDVS ID:%llx: iohideventsystem_client_dispatch_virtual_service_set_property:%x
Invalid reply from PowerD\n
IOHIDEventServerUnschedule
No policies defined for this process
Failed to create XPC message\n
Powerd has requested assertion activity update
Invalid reply type\n
Powerd knows about this assertion 0x%0x. let powerd time it out
assertion failure: \"pthread_mutexattr_init(&mutexattr)\" -> %llu
fetchAssertionCategoryPolicies: Reply is not a dict
No timeout ts. Remove from timed list
Unable to serialize event
invalid io_service_t for %@
assertion failure: Failed to create notification port %p
Service removed: %{public}@ %@
io_hideventsystem_set_properties:0x%08x result:%d
%@ is not serializable. result: %@
SetProperty called %@=%@ caller=%@
0x%llx: IOHIDResource not found
processAssertionTimeout: Removing from gActiveAssertionsDict: 0x%x
handleAssertionTimeout fired %llu
Event handler is called %@\n
__IOHIDServiceCreateObjcServicePlugin Failed to initialize plugin
assertion failure: \"pthread_cond_init(&session->stateCondition, ((void*)0))\" -> %llu
Timeout: assertion id 0x%x with time %llu, policy timeout %llu
Set cursor enable:%s
IOHIDEventSystemAddServices
Unknown client type: %d pid:%d
Failed to create xpc msg object\n
No connection to powerd
Failed to release assertion 0x%x on timeout
Invalid type
Bad matching dict
assertion failure: \"!manager->runLoop && !manager->dispatchQueue\" -> %llu
io_service_t has no IOCFPlugInTypes for %@
thread_id=%p
IOHIDEventQueueNotify:%#x
Failed to find %s for copy domain, switch to default CFPreferences
Add filter:%@ for service:0x%llx
Assertion has a policy category timestamp %@
Could not load TCC
IOHIDEventSystemServer died. Reestablishing connection.
assertion failure: IOConnectMapMemory:0x%x
Found timeout %@ for category string %@
powerd released our connection
IOPMAssertionCreateWithProperties: Call to io_pm_assertion_create failed with kernel error 0x%x
IOHIDSessionFilterCreateWithClass Failed to initialize filter
Received termination imminent error for connection 0x%lx
IOHIDEventSystemCreate
Service: %@ cancellation timer timed out
Assertion index 0x%x already exists
Unable to allocate acquire client reply port attributes
bootstrap_look_up_per_user failed: %s
powerd returned err 0x%x to create assertion %@. Dropping the assertion\n
processAssertionTimeout: Turning off assertion idx:%d id:0x%x
Unexpected message from async assertions connections\n
%s: HIDVS ID:%llx iohideventsystem_client_dispatch_virtual_service_copy_property:%x
Failed to load %s
HIDVS (id:%llx) invalid parameters
Releasing assertion locally id 0x%x
HIDVS (id: %llx) invalid event data
Async sssertion bufffer initialized.
CFPlugInFindFactoriesForPlugInTypeInPlugIn failed for plugin url %@ for %@
0x%llx: kIOHIDResourceDeviceUserClientMethodHandleReport:%x
%s: Filtered event type:%@ sender:%#llx eventInfo:(%@) -> outEventInfo: (%@)
%s: HID activity: start reporting with interval: %ds
no event->parent->eventData
IOHIDConnectionFilterCreate Failed to find HIDConnectionPlugin protocol
Connection added: %{public}@
0x%llx: __IOHIDServiceInit creating queue with high-priority QOS
IOHIDServiceFilterCreateWithClass failed for bundle %@
Failed to find %s for set domain, switch to default CFPreferences
IOHIDConnectionFilterCreate failed to find symbol %@ for bundle %@
IOHIDEventSystemCreate error
IOHIDSessionOpen
Unable to create IOHIDEvent with length:%d
%s: iohideventsystem_client_dispatch_event_filter:0x%x
Powerd has requested active assertions update
IOHIDSessionFilterCreateWithClass class does not conform to SessionFilter protocol
event system =\n%s
assertion failure: Failed to get async event source: 0x%x %p
IOServiceGetMatchingServices:0x%x
%s: Server died, preventing any future MIG calls
%s: iohideventsystem_client_dispatch_properties_changed:0x%x
%s: HID activity: %d -> %d (service:0x%llx event:%d)
%s: Unable create activity notification
Set cursor enable failed:0x%x
Failed to create connection\n
assertion failure: \"pthread_mutex_init(&service->queueContext->lock, &mutexattr)\" -> %llu
IOHIDSessionFiltersClose
0x%llx: __IOHIDUserDeviceStartDevice:0x%x
IOHIDEventServerCreate
Invalid SampleInterval: %@
No current assertion. Sending all activity till now
IOCreatePlugInInterfaceForService:0x%x for serviceID:%#llx
Set fixed mouse location failed:0x%x
SecTaskCreateWithAuditToken failed for pid:%d
Category %@ not found
Not a dictianary for 0x%x
Failed to update machport for IOPMConnection id 0x%x. rc:0x%x\n
Unable to create event attachment storage
0x%llx: kIOHIDResourceDeviceUserClientMethodPostReportResponse:%x
plist invalid for pluginType %@
assertion failure: \"!manager->cancelHandler && handler\" -> %llu
__IOHIDEventSystemCreateNotification
assertion failure: \"semaphore\" -> %llu
__IOHIDEventSystemRelease
HIDVS (id:%llx) invalid property key
Unable to create event queue via hidd: (%08x)
IOHIDServiceFilterCreateWithClass class does not conform to HIDServiceFilter protocol
Not a dictinary for 0x%x
No assertion dictionary or logging data to send
XPC event: %@\n
mach_port_deallocate(bootstrap_port) %s
Checking getTimeout for string %@
Turning off assertion 0x%x: %@
IOHIDEventCreateDigitizerEvent event is null
HID Event System Client refreshed but no services returned
%s: HIDVS ID:%llx iohideventsystem_output_event_to_virtual_service:%x
Unable to serialize matching data
Session Filter:%@ filtered copy event (service:0x%llx, type:%d)
assertion failure: \"queuePort\" -> %llu
IOHIDServiceFilterCreateWithClass Failed to find HIDServiceFilter protocol
%s: Unable to create DISPATCH_SOURCE_TYPE_MACH_SEND for reply port
Resuming timer
Removing 0x%x from TimedList
Received an error in response to IOPMCopyActiveAsyncAssertionsByProcess
0x%llx: Unable to create queue analytics
Async assertion created with 0x%x, length %ld, %@\n
processAssertionUpdateActivity: No gAssertionConnection
Assertion retain not supported in async mode\n
IOHIDSession close completed
Unexpected data type in gAssertionsDict for id:0x%x\n
Sending Assertion release message for assertion Id 0x%x\n
xpc_user_sessions_get_foreground_uid failed: %d - %s
Unable to map event queue: (%08x)
Setting category timeout timestamp to %@, monotonic time %llu
Failed to send IOPMConnection request. rc:0x%x\n
Initial connection to powerd not setup
Failed to create event at index=%d , eventDataMaxSize: %u < eventDataSize: %u
gAsyncModeDisableOverride: enable
bootstrap_look_up2 failed: %s
mach_port_deallocate(server_port) %s
CreateSessionFilterClass
Connection: %@ TCC check for service %@: %@ returned right:%llu
Failed to create gAssertionConnection\n
assertion failure: \"client->notifyPort\" -> %llu
IOHIDEventSystemRelease
0x%llx: Packet size is to small for large report, but large report flag is set. reportFlags:%#x entrySize:%u
Set on screen cursor bounds failed:0x%x
assertion failure: \"retainCount < (2147483647 *2U +1U)\" -> %llu
%s: HIDVS ID:%llx iohideventsystem_copy_matching_event_from_virtual_service:%x
IOHIDEventSystemOpen:%lldus
assertion failure: \"pthread_mutex_unlock(&(session->queueContext)->lock)\" -> %llu
__IOHIDServiceLoadObjcServicePlugin failed to find symbol %@ for bundle %@
0x%llx: get report not handled
_IOHIDCreateBinaryData: %@
Checking for timeout for category %@ %d
Received assertion activity update refcnt %u overflow %d
Client must be scheduled with dispatch queue or runloop
IOHIDSessionUnschedule
Failed to convert XPC to CF object\n
Async assertion: setting offload delay to %llu
IOPMAssertionCreateWithProperties: io_pm_assertion_create failed with error 0x%x
io_hideventsystem_remove_virtual_service:%x
0x%llx: os_workgroup_interval_finish error: %d, service %@
__IOHIDServiceCreateObjcServicePlugin Failed to find HIDServicePlugin protocol
0x%llx: Set report interval current:%d new:%d result:%d events:%@
offloadAssertions fired
0x%llx: set property:%@ value:%@ client:%@
Set cursor bounds failed:0x%x
assertion failure: \"pthread_mutex_init(&session->queueContext->lock, &mutexattr)\" -> %llu
insufficient buffer data available, size: %ld, length: %ld
0x%llx: IOHIDServiceSetElementValue time:%lluns
0x%llx: Set batch interval current:%d new:%d result:%d
Add session filter:%@
Invalid ptr=%p size=%d.
IORegistryEntryIDMatching:NULL
Category %@ has a policy %@
start failed (%s) for plugin for %@
CFPlugInCreate failed for url %@ for %@
Failed to register for reconnecting with powerd. rc:0x%x
0x%llx: Failed to open service
sendAsyncAssertionMsg failed: powerd xpc connection interrupted
bundle invalid for pluginType %@
XPC event handler: %@\n
posting reset to (%p)(%p, %p)
setAsyncAssertionProperties for 0x%x %@:%@
Failed to find %s for copy multiple, switch to default CFPreferences
no factories for plugin for %@, kr = 0x%x, factories = %p, factoryCount = %ld
Failed to create event at index=%d , eventDataSize: %u < minimum size: %u for type: %u
Enabled flag not found\n
IOHIDConnectionFilterCreate class does not conform to HIDConnectionPlugin protocol
assertion failure: Unschedule failed queue: %p runLoop: %p
QueryInterface:%x
Error: the client with pid %d is missing the '%s' entitlement.
Received assertion category policies from powerd %@
Assertion 0x%x has already been released
assertion failure: \"pthread_mutex_unlock(&(queueContext)->lock)\" -> %llu
%s: HIDVS ID:%llx create
Logging all %ld activity to powerd\n
handleAssertionTurnOff: Released assertion id 0x%x
Failed to find %s for copy, switch to default CFPreferences
assertion failure: \"client->queuePort\" -> %llu
0x%llx: unschedule from runloop completed
Assertion feature: setting gAsyncMode to %d
IOPMAssertionCreateWithName: One of the arguments is NULL
IOHIDEventSystemCreate:%lldus
IOHIDEventSystem TCC matching: SecTask code sign status SPI unavailable, gating disabled
IOHIDEventSystem TCC matching: tcc_authorization_check_audit_token unavailable, gating disabled
assertion failure: \"pthread_mutexattr_destroy(&mutexattr)\" -> %llu
IOHIDSessionCreate failed to find symbol %@ for bundle %@
IOHIDSessionClose
%s: mach_port_request_notification(notify):%s
%s: HID activity: stop reporting
Unable to create analytics description
Failed to create gAssertionsDict
IOPMAssertionCreateWithProperties: pm connection failed
IOPMAssertionCreateWithProperties: Failure copying assertion properties. Collect backtrace %llu
handleAssertionTimeout: Setting assertion timeout to fire in %llu secs
Received active assertions from powerd %@
IOServiceMatchPropertyTable failed for url %@ for %@
assertion failure: \"pthread_mutex_lock(&(session->queueContext)->lock)\" -> %llu
failed to create instance for plugin for %@
Unable to allocate set client reply port attributes
0x%llx: IOServiceOpen:0x%x
Missing state in reply\n
IOHIDSessionUnregisterServices
IOHIDSessionSchedule
IOHIDSessionRegisterFilters
%s: HIDVS ID:%llx _iohideventsystem_copy_event_from_virtual_service:%x
Session Filter:%@ filtered copy event (service:0x%llx, type:%d, new type:%d)
Fail to set parameter with status 0x%x
assertion failure: \"!device->cancelHandler && handler\" -> %llu
0x%llx: IOHIDServiceRequestTerminate
%s: iohideventsystem_client_dispatch_service_removal:0x%x
Initial level is off for 0x%x: %@
io_service_t has invalid IOCFPlugInTypes for %@
Failed to create message\n
__bootstrap_status:0x%x
[%#llx] Invalid kIOHIDTCCServiceKey property, expected String
No AssertionActivity in xpc reply
Failed to create useractiveRefs
IOPMAssertionCreateWithProperties: One of the arguments types is incorrect
HID Session async scheduling complete.
Sending initial message to powerd for async assertions
processAssertionTimeout: Not found in gActiveAssertionsDict: 0x%x
Failed to create dictionary to send message\n
Failed to create event system client
Failed to create XPC connection\n
_IOHIDCreateBinaryData fail
createAsyncAssertion: async mode disabled due to SmartPowerNap
Failed to find %s for set multiple , switch to default CFPreferences
Failed to create server dipatch queue
HID Event System Client refreshed with %ld services, cached matching had %ld services
EventForClient filtered type:%d sender:0x%llx eventInfo:(%@) service filter:%@ for client:%@
%s: mach_port_allocate(sendPossiblePort):%s
Setting assertion timeout to fire in %d msecs for timeout_ts %llu
Created IOPMConnection with id 0x%x\n
Current assertion has been released by powerd gCurrentRemoteAssertion 0x%x gCurrentAssertion 0x%x
Failed to create XPC connection to PowerD\n
IOCreatePlugInInterfaceForService:0x%x
0x%llx: set report interval:%@ client:%@
IOServiceAddMatchingNotification:0x%x
%@ is not serializable
Shipping charge limit data not found\n
Client record is not serializable for %@
0x%llx: set report not handled
Failed to get UUID. rc=%d\n
HIDVS (id:%llx) client does not exist
Failed to create xpc objects to send userActivityRegister message\n
unexpected policy request %llu
invalid matching dictionary: %@
assertion failure: Activate failed queue: %p runLoop: %p
Connection: %@ not entitled to match protected service: %@
0x%llx: close completed
Unable to allocate queue object via _CFRuntimeCreateInstance
level_change through kIOPMAssertionLevelKey write.
offloadAssertions called with gCurrentRemoteAssertion 0x%x
assertion failure: Invalid dispatch state: 0x%x
IOServiceAddInterestNotification: 0x%x
Setting gAssertionsOffloader timeout to %llu\n
Failed to create the remoteID to CF for id %@\n
Released connection: %s\n%{public}@
io_hideventsystem_queue_start:%#x
0x%llx: Start: %@
bootstrap_check_in() failed: %s
IOHIDEventSystem TCC matching: could not load Security.framework, gating disabled
gAsyncModeDisableOverride: disable
Timeout from category %d
setAsyncAssertionProperties: Failed to get the assertion details for id:0x%x\n
level_change->true through kIOPMAssertionTimeoutKey write on an inactive assertion.
Failed to send mach port for IOPMConnection id 0x%x. rc:0x%x\n
Unable to open %#x
FilterEvent filtered type:%d service:0x%llx eventInfo:(%@) session filter:%@
Received an error in response to copy '%s' data\n
0x%-16llx 0x%-16llx 0x%-16llx 0x%-16llx 0x%-16llx
called with a NULL callback
Entry of IOHIDService property %s incorrect type: %@
0x%llx: Unable to create analytics description
logAsyncAssertionActivity: unable to find assertion with id 0x%x
Failed to find %s for create
Irrecoverable error for assertion creation\n
Assertion 0x%x is neither active nor turned off
Virtual service (id: %llx) does not exist
IOHIDSessionFilterCreateWithClass failed for bundle %@
0x%llx: Destroy: %@
%s: mach_port_deallocate(unusedNotify):%s
io_hideventsystem_do_client_refresh:0x%x
%s: Event enqueue dropped:%d consecutive events
%s: HIDVS ID:%llx destroy
processAssertionTimeout: Removing idx:%d id:0x%x
assertion failure: \"retainCount\" -> %llu
IOHIDEventSystem TCC matching: could not load TCC.framework, gating disabled
Malformed PropertyMerge value in bundle: %@
HID Session async scheduling initiated.
All actions on enumeration queue completed.
CFDictionaryCreateMutableCopy fail
Failed to create dictionary to send message
No plist for plugin url %@ for %@
CreateSessionFilter
IOHIDEventSystemOpen error
Service added: %{public}@
Bad arguments
unable to make mach memory entry. (%08x)
Failed to get DeviceUsagePairs: %@
IOConnectGetService Failed with err : 0x%x
API will be deprecated soon.  Please use IOHIDEventSystemClientCreate.
Suspending timer
IOHIDSessionFilterCreateWithClass Failed to find HIDSessionFilter protocol
Unable to get serviceID for IOHIDServiceClient: %@
IOPMUnregisterNotification: cancelling connection 0x%lx\n
sendAsyncAssertionMsg failed: powerd xpc connection invalid
EventToConnection filtered type:%d service:0x%llx connection:%@ session filter:%@
No timeout for category %@ for policy %@
powerd returned assertion id 0x%x for async id 0x%x \n
Fail to get parameter with status 0x%x
unable to create dictionary
Failed to create event at index=%d , eventDataSize: %u < sizeof(IOHIDEventData): %lu
IOHIDEventSystemOpen
Loading symbol for principal class:%@ from bundle
[%s] Process has entitlement %s on Non-Internal build
Wake progress from %d. data: 0x%x\n
IOHIDEventSystemClose
Connection: %@ denied match of service %@: TCC %@ right:%llu
0x%llx: set batch interval:%@ client:%@
%s: mach_port_request_notification(MACH_PORT_NULL):%s
Received processCheckAssertionMsg with active assertion 0x%x
Failed to get PM queue\n
__IOMIGMachPortRelease mach_port_mod_refs:%s
Failed to register for %s
IOHIDService compatibility thread running at priority %d and schedule %d.
HID Session async root queue running at priority %d and schedule %d.
Failed to create xpc reply object\n
Missing key '%s'\n
Recreating IOPMConnection id 0x%x\n
IOHIDSessionRelease
Unable to retain service: 0x%x
Registering for assertion policy changes
handleAssertionLevel: unable to find assertion with id 0x%x
pluginPath == NULL, unable to allocate a CFString
assertion failure: \"!queue->cancelHandler && handler\" -> %llu
IOHIDConnectionFilter
SupportsCollectionEvents
%s created from m%s is missing its info dictionary.
com.apple.system.powersources.source
UNKNOWN
Unload
TimingStandard
Wake On Modem Ring
ActivityTimeout
OSKextIdentifierCacheBasePath
TPS1
Reduce Processor Speed
Stylus
userDeviceQueue
Failed to create lookup address object.
PolicyTimeoutTimeStamp
SystemIsActive
IOKit IOGetSystemLoadAdvisoryDetailed
{\n
chargeSocLimitAction
Open failed for %s - %s.
Successfully stopped %s.
Authenticating %s file/directory %s.
DolbyVision (native)
SMPTE 170M/BT.601
IdleSleepPreventers
%-20.20s 0x%016llX NON KERNEL SENDER\n
W:
Creating %s.
? Gbps (Unknown FRL rate)
80-bit custom pattern
Branch
<false/>
Total Latency:
%-20.20s 0x%x\n
<IOHIDUserDeviceRef ref:%d/%d id:0x%llx stats:%d,%d,%d>
Hot Plug
chargeSocLimitIsEOC
_IOHIDServiceCreate_block_invoke
filterEvent:forClient:
Transition: Enter
IOHIDEventSystemClientDispatchQueue
VFTG
MaxState
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
Compatible version must be lower than current version.
Transport:
PortType
StartLink
WakeRelativeToSleep
UPSShutdownAfterMinutes
%s is already open; returning existing object.
com.apple.private.hid.client.event-dispatch
0
Omitting loaded kext %s from mkext for kernel load.
%s failed to compress executable.
kr == KERN_SUCCESS
Thermal_Level_Warning
DeviceUsagePairs:
ConnectionPluginDebug
Link Training Command
Internal error, invalid argument to __OSKextCheckURL.
UPSShutdownAtLevel
PrioritizeNetworkReachabilityOverSleep
EnergyMode
batteryGaugingMitigationState
chargeSocLimitSoc
SCError
now
OSBundlePath
%@%@/%@
The kext contains a symlink which is either not readable or points outside of its bundle; please remove
D10.2
Timestamp
MinLinkRate
[^/]+
NormalizedPositionDeltaX:
Built-In
OSBundleStarted
/Library/Extensions
Wake On AC Change
IODeviceTree:/product
%s.IOHIDUserDeviceRef
InterfaceRole
/System/Library/AppleUSBDevice/USBDeviceConfigurationOverride.plist
ButtonMask:
Kext identifier->cache for %s - cache version missing/invalid.
Failed to create directory %s - %s.
IOSleepSupported
setDispatchQueue:
Cache file %@ does not exist.
Stat failed for %s - %s.
Start
Passthrough-only
ClickSpeed:
Executable does not contain code for architecture
IOCFSerialize
%s\n
ServiceID
%@/%@
score
mkext data
com.apple.iokit.cfplugin
assertion failure: Manager has already been activated/cancelled.
EventFilterTimeoutCount
/usr/appleinternal/lib/HIDPlugins/SessionFilters
MaxPower
Video Color
IOCFSerialize.c
com.apple.system.powersources.timeremaining
Progress
LatencyServiceOpen
RegistryID
NameChange
Accelerometer
LatencyServiceInit
initWithService:
w
%08x: 
Front Right
TransitionTime,us:
assertionTimeout
sentinel %qx\n
AmbientLightSensor
ProductID:
DSC:          YES (%f bpp, passthrough)\n
claimSystemWakeEvent
cursor
assertion failure: Queue already scheduled
Position 
File not found
(unknown error)
_MKEXTExecutableRelativePath
Rear Center
DolbyVision (HDMI tunneling)
CountryCode:
filterEvent:forService:
%F %H:%M:%S
initWithConnection:
UPSShutdownAtMinutesLeft
HIDResetPointer
/System/Library/Extensions
---------------------------\n
assertionUpdateActives
1:1
%s:%s%s%s%s%s%s%s
Can't read kernel CPU info from IORegistry (absent or wrong type).
VGA
kext
Realizing %s from identifier cache object.
Button Mask:
Driver Extensions may not use the %@ key; please remove.
Color Attributes:\n
27:64
IOAppPowerStateInterest
SCPreferencesLock
GenericGesture
Repeat:
deviceSubClass
CurrentState
DesktopMode
Face Button A:
MayBegin
Local-Root
HIDPointerAccelerationType
pid
CompleteLink
Transition: Exit
Flushing dependencies for %s.
 authentication
OSBundleLoadTag
 not
OSBundleAllowUserLoad
IOProbeScore
%-20.20s %f\n
LongSqueeze
Only incompatible kexts found for these libraries
HIDPreferencesSynchronize
batteryKioskModeData
RunLoop
Squeeze
IOHIDService.c
%s - dependency for %s lacks valid OSBundleCompatibleVersion.
not
Interlaced:    %s\n
Humidity
Brightness
Joystick Axis Rz:
DeviceUsagePage
Adding IOBundlePublisher %s to %s personality %s.
MPEG2
HIDCapsLockLED
IOPathMatch
%3lld%c 
Front Left Center
(invalid)
%-20.20s %@\n
Personality CFBundleIdentifier names a kext that is not loadable (run kextutil(8) on it with -nt for more information)
Cache file %@ is out of date; not using.
HIDAnalyticsEventAddHistogramField
WakeByCalendarDate
Can't create kext: missing or non-string version in identifier cache entry %d.
%s: internal overrun in executable file (%s).
RestartInterfaces
SleepDisabled
client
Down:
TransducerType:
Driver Extension lacks appropriate value for OSBundleRequired, and will not be launched without kextd present. Use one of 'DriverKit' or 'Safe Boot.'
Front Left High
AdobeRGB
Twist:
OSBundleUUID
__OSKextCreateKextsFromURL
, UUID 
TimeoutActionRelease
TCCAccessRequest
state.dataIDRefDictionary
clientNotification:added:
IOResources
DroppedEventCount
TurnedOff
Front Right Wide
%-20.20s 
Face Button X:
Failed to parse kernel log messages: %s.
%-20.20s 0x%016llx\n
16:10
UsagePercent
serialNumber
bootstrap_look_up2 failed with 0x%x\n
IOHIDValue
 %@=%@
LongPress:
HIDObjectUUID
notificationCount
Load
%s is not valid; omitting from mkext.
IOAVDevice
IOHIDEventSystemClientDispatchMach
assertion failure: IONotificationPortCreate
.XXXXXX
Failed to read contents of %s, CFURL error %d.
zlib inflate failed: %s.
State
GRGB Tunneled as YCbCr422 (Even line red)
Dependency Resolution Failures
Dynamic Range & Mastering
default
Flushing info dictionaries for all kexts.
Detailed
18 Gbps (6Gbps/lane * 3 lanes)
wakeData
XYZ
Probability:
***UNKOWN***
Can't stat source folders for cache file %@.
Reserved
NXSystemInfo
fastpath
unknown error
Requesting unload of %s%s.
ID = \"%@\"
EventFilteredCount
assertionActivityUpdateOverflow
StopInfoFrame
Failed to set permissions for %s - %s.
%s%s (%s)%s
Delay Autounload
AppleSecurityExtension
%s: %lld\n
forward reference detected
net 
ZoomToggle
 (dependencies not resolved).
OSKext
Scan Type:     %s\n
Full
Path
com.apple.iokit.ioserviceauthorized
Performance_Warning
IOUSBDeviceController
HIDKeyboardModifierMappingSrc
Timestamp type:
ElementData
HIDPreferencesSetMultiple
HighPowerMode
Unit
IOKit Power
PortVariant
HDCP2
0x%lx
Carrier Mode
batteryShippingChargeLimitAction
Location:
Can't create kext: missing or non-string bundle package type in identifier cache entry %d.
DSCRequiredColorElementIDs
%@
LastPropertyNotificationTime
Class
GetReportCnt
Finished reading cache file %s.
Statting %s for map.
zlib inflate discrepancy, uncompressed size != original size.
assertionProperties
PresentPassive
ReportInterval:
DolbyVision LL YCbCr 4:2:2 (HDMI tunneling)
HIDPreferencesCopyDomain
string
Standby Enabled
HIDSubinterfaceID
SCDynamicStoreAddWatchedKey
Lane %d:\n\n
ConfigurationType
YCbCr 4:4:4
builtin-battery
AbsentWithDisplay
Matching
/AppleInternal/Library/Extensions
14:9
Extra Button L4:
propertyCacheMiss
IOKitPersonalities
%s, version %s removed from identifier lookup dictionary.
Dynamic Power Step
RestartAfterKernelPanic
description
Kext declares both CFBundleExecutable and CFBundleSharedExecutableIdentifier; use only one.
size=\"%d\"
matching
Failed to read requests from kernel - %s.
PortNumber
SenderID:
Can't determine actual safe boot mode - sysctl() failed for KERN_SAFEBOOT - %s.
AssertName
Audio Stream Data:\n
Sender
DispatchQueue
DockSwipe
YCbCr 4:2:2 (HDMI tunneling)
state.tags
IOHIDUserDevice
HIDIdleTimeMicroseconds
Kext library architecture set to %s%s.
Can't stat %s - %s.
</key>
Mobile Motion Module
...(%u bytes total)
Inactive
Kext has a CFBundleExecutable property but the executable can't be found
Can't read file %s.
Hibernate Free Ratio
SCDynamicStoreCreate
AngleDegrees:
TimedOut
InstanceMetadata
HIDResetKeyboard
%-20.20s %llu\n
Pressure:
Accuracy:
BatchInterval
com.apple.kernel.unsupported
NO
Dispatch Latency:
assertion failure: IODataQueueAllocateNotificationPort
!parent
oflag
SleepFailure
vid 
ElementCookie
assertion failure: Device has already been activated/cancelled.
propertyCacheHit
assertionActivityUpdateRefCnt
PrimaryUsage
MotionGesture
NormalizedPositionX:
Can't create kext from cache: non-boolean OSKextEnableKextLogging in identifier cache entry %d.
Can't create kernel load request for %s.
state.arrayIDRefDictionary
Product
Range:
IOHIDEventServer
Memory allocation failure.
Caller
/Library/Apple/System/Library/HIDPlugins/ServiceFilters
SensorPropertySupported
DSC:          YES (%f bpp, decompress)\n
HDMI
Category
ColorSpace:
DeviceUsage
Queue
assertionCheck
WakeDisplay
Hibernate File
qos
assertionCheckCount
Score
SCDynamicStoreCopyValue
NormalizedPositionY:
Attributes
AC3
ShipChargeLimitData
ConnectionEntitlements
StopLink
Protection Command (with source and AUP data)
Audio Channel Layout
IOHIDTransaction
Can't record kext in identifier lookup dictionary; no identifier.
ProtectedServicesDisabled
HIDPreferencesSetMultipleForInstance
IOAccessoryHSAIDBulkData
com.apple.powermanagement.assertionexception
Dolby Atmos (MAT2.0)
IOHIDServiceConnectionCache
SCDynamicStoreKeyCreatePreferences
Kexts already loaded for these libraries have no OSBundleCompatibleVersion
BatteryPacks
<%s IDREF=\"%d\"/>
chargeSocLimitReason
LatencyEventSystemCreate
Unable to determine realpath for %s - failing.
.hid
service
%s is not valid.
Failed to start %s - %s.
Loading %s.
Internal
chargeSocLimitDrain
HIDScrollAccelerationType
ConfigurationDescriptors
Selectable
SleepWakeUUID
IOHIDEventSystem
Administrative
Info dictionary property value is of incorrect type
Kext identifier->path cache for %s is up to date.
IsPreferred
IOService:/IOResources/IOHIDSystem
HIDPointerButtonMode
Monitor
'%@' -> '%@'
Can't create %s - %s.
HIDPreferencesSet
IsLowPower
Phase
LogIOHIDFilteredEvents
Ry:
%s not found in identifier lookup dictionary%s.
AudioChannelLayoutElements
Capture
batteryShippingChargeLimitEnable
Dependencies have validation problems
%s has no personalities to send to kernel.
QueueState
matchConnection:
OS
Kext personality for kext %s is not a dictionary
MaxPropertyNotificationHandlingTime
usagePage: %ld usage: %ld children: %ld ungroupForLegacy: %ld
%-20.20s %s%s\n
MinorRadius:
Kext identifier->path cache for %s - kext entry not a dictionary.
FrameworkBundleID
UUID
staticSize
Power
ClientEventFilter
Reading load info for all kexts.
ActivityTime
Other
SwipeLeft 
com.apple.powerd.assertionoffloadtimer
IOPCITunnelCompatible
WakeOnMagicPacket
HIDKeyRepeat
CH3:
ElementType
Rear Right Center
scRGB
com.apple.system.IOPMSchedulePowerEventNotification
systemAssertionTimeout
DidUpdateMask:
Changed
Successfully unloaded %s.
assertionSetState
SessionFilterDebug
Value
Simple
DeviceUsagePairs
com.apple.userspace_ethernet
Interface kext must have exactly one dependency.
Symbol Error Rate Measurement Pattern
chargeSocLimitToken
Failed to map executable file %s (offset %lu, %lu bytes) - %s.
Load audit function returned false, bailing on adding %s to mkext.
IOUserClass
HIDPreferencesCreateInstance
Joystick Axis X:
IOHIDEvent Server Connection - Root
Failed to load %s - %s.
HIDDebug
IOHIDEventService
Kext Request Lookup Address
%s adding implicit Kcov dependency
/IOKit/Power
Kext isn't loadable during safe boot.
, DSC (%f bpp, passthrough)
idRef
chargeSocLimit
reason
Personality matches on IOResources but IOMatchCategory is missing or not equal to its IOClass; driver may be blocked from matching or may block others
Failed to read kexts requested by kernel since startup - %s.
StartInfoFrame
5:4
/System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
Flushing info dictionary for %s.
Protected
rh:
Removed %s, id %s%s, version %s.
Internal error in diagnositcs recording
%s added %u-byte %scompressed executable to mkext.
External
<%s ID=\"%d\" %s>
/IOKit/PowerManagement/SystemLoad/Detailed
Attempt to set 64-bit load address - %s.
HIDPreferencesCopyMultipleForInstance
SleepServiceImmediate
setCancelHandler:
setting load address of %s to 0x%0x
Interfaces
ForceStage
%@ is not a system extensions folder; not looking for a cache.
sRGB
MobileMotionModule
Scroll
Multiple kexts for these libraries occur in the dependency graph
Finished reading identifier->path cache for %s.
Saved cache file %s.
IOCircularDataQueueCreateWithConnection
IORegistryEntryID
Stop 
procName
Kext logging %sabled for %s.
com.apple.kernel.6.0
Kernel load info for %s lacks a CFBundleVersion.
Enhanced Mode: %s\n
HIDNumLockState
UsagePage
assertionId
Top Center
IOProviderClass
IOHIDServiceFilter
/usr/appleinternal/lib/HIDPlugins/ServiceFilters
Unsupported
active
Details
IsPromoted
syntax error
Display Sleep Uses Dim
HIDKeyMapping
assertion failure: Dispatch queue already set
 for:
Get Loaded Kext Info
Can't load %s - a different %s is already loaded.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n
DYLD_IMAGE_SUFFIX
No load audit function set, cannot load %s
Architecture %s not found in mkext.
HIDAnalyticsHistogramEventSetIntegerValue
9:15
Overscan
AppleLSIFusionSAS
IOService
serviceplugin
FluidTouchGesture
Right Headphone
v24@?0^v8^v16
9:14
MIPI
HIDInterfaceID
Unicode
%s - no compatible dependency found for %s.
runloop
Released
Vendor Specific Data Block
GTF
ProximityDarkWake
Architecture %s not found by CPU info (type %d, subtype %d), trying by name.
KeyboardLanguage
TTYSPreventSleep
StageProgress:
NextEventTimeStampDelta
CPU_Power_Limits
PreventUserIdleSystemSleep
Created
productString
DefaultDeviceDescription
property
Kext is a kernel component but OSBundleIsInterface is set to false; overriding
Kexts may not use the DriverKit value for OSBundleRequired.
Requests from kernel missing or of wrong type.
%s
Can't load %s - validation problems.
type
/Library/Apple/System/Library/HIDPlugins
AVI
IOHIDService(%p) id:0x%llx name:%s
Format: %s Channels: %d SampleSize: %d SampleRate: %d hz\n
Close
%s (version %s%s%s) is loaded.
/AppleInternal/Library/HIDPlugins
propertyForKey:client:
DequeueTimestamp
EjectDelay
GPUSwitch
f
com.apple.system.powersources.percent
__LINKEDIT
OBJC_CLASS_$_%@
VersionNumber
Stop
PreciseAspectRatio
CalibrationGranularity
Can't rename temp cache file to %s - %s.
failed to open io_service_t err=0x%x
Collection
Reading load info for %u kext%s.
AppleClamshellState
CVT
%@#%@#%@#%@#%@
%-25.25s %f\n
Left Headphone
IOPersonalityPublisher
com.apple.private.hid.client.event-filter
Hidden
HIDCapsLockState
LatencyDispatchEvent
Thumbstick Button Right:
SecTaskCreateWithAuditToken
com.apple.iokit.iomigmachport
 }
com.apple.iokit
HIDInitialKeyRepeat
Touch 
HandleReportCnt
IOAVAudioInterface
WMAPro
IOCircularDataQueueImplementation.h
SerialNumber
v12@?0I8
IOHIDManager State
lastNotifyTime
AllowsDeviceRestart
Bluetooth
EventType
%s, version %s recorded at index %d in the identifier lookup dictionary.
Mkext plist compressed size is %u.
TPS3
IOHIDNotification
OSBundleRequired
Failed to serialize kext request.
Found %s.
AppleLSIFusionSCSI
IOHIDManager
AttributeDataLength:
IOHIDEventQueue
com.apple.kernel.
IOHIDLibPrivate.c
EnableIdleSleep
MP3
object
&gt;
oversized
AttributeData:
%@ - %@
PrimaryUsage:
DeviceUsagePage:
HandTap
Automatic
not serializable
TouchSensitiveButton
ForceActive 
Error communicating with kernel - %s.
ICH8 ATA/100
SCPreferencesApplyChanges
Reading resource file %s%s.
com.apple.kpi.unsupported
time
Shake
Boot Level Restrictions
%s has %d remaining undefined symbol%s
AppleEmbeddedSleepWakeHandler
state.numberIDRefDictionary
<IOHIDDevice %p [%p]  'ClassName=%s'
setProperty:forKey:client:
IOUserEthernetResource
Personality CFBundleIdentifier names a kext that doesn't declare an executable
/usr/appleinternal/lib/HIDPlugins/ServicePlugins
Unregistered
true
Ethernet
Temperature
Ungroup for legacy clients
Can't open cache file %s, CF error %d.
deviceClass
AAC
assertionCheckToken
SMPTE ST 2084 (PQ)
IOCFPlugInTypes
IONetworkInterfaceProperties
SCPreferencesCreate
SCPreferencesUnlock
Version:
WillUpdateMask:
Cache file %@ - group not wheel; not using.
AsyncRemoteAssertionId
DoubleSqueeze
ReleasedThreshold:
AppleKernelExternalComponent
AssertionOnBehalfOfPIDReason
IOCFUnserialize: can't alloc temp memory
Creating kexts from identifier->path cache for %s.
    
unexpected end of buffer
false
IOPSPrivateBatteryHealthState
PowerManagement
MaxPropertyGetTime
IOEthernetController
String/URL conversion failure.
<key>
batteryChargingIconoGraphyState
Failed to get file info (stat failed)
userActivityRegister
ServicePluginDebug
Vendor Specific
ServiceFilterDebug
Searching for link dependencies of %s.
USB
Kexts with a kernel library < v6.0 must set MODULE_NAME the same as CFBundleIdentifier to load on kernel < v6.0.
Can't create kext cache under %s - owner not root.
CarrierChargingMode
v12@?0C8
Kext personality %s subentry is not a dictionary
, no UUID
HIDPreferencesSetForInstance
addStartTag
propertyForKey:
Opening %s for map.
status
Can't parse info dictionary XML
Kexts already loaded for these libraries are not compatible with the requested version
DolbyVision LL YCbCr 4:4:4
com.apple.iokit.statenotification.create
UPSDefaultThresholds
AppleSmartBatteryManager
CFBundleIdentifier
/Library/Apple/System/Library/Extensions
assertionUpdateCategoryPolicy
PRBS7
/var/vm/sleepimage
PowerByCalendarDate
displayUUID
deviceID
Link Command
d
Passive
Kext is not signed
&lt;
getBatteryHealthState
FullWake
4:5
VESA
DisplayDims
HIDClickTime
Sequence:
Kext declares no kernel/KPI libraries; if it references any kernel symbols, it may fail to link.
TimingType
Carrier Mode High Voltage
HIDWaitCursorFrameInterval
,
com.apple.iohidmanager
Irregularity:
Failed to stop %s - %s.
ATRAC
FIXME: IOUnserialize has detected a string that is not valid UTF-8, \"%s\".
Digitizer
uniqueDeviceID
IOSystemStateNotification
ReduceBrightness
wakepoweron
EstimatedPressure 
IOHIDService Enumeration - Root
Can't create kext from cache: %s is already open and has a different CFBundlePackageType from identifier->path cache entry %d.
Personality
SystemSleepPreventers
Transport
Scale
IOAVControlInterface
/IOKit/LowBatteryWarning
Transport Type
momentum:
Can't read mach-o file %s.
com.apple.system.powermanagement.assertionresync
Attribute 
com.apple.hid.analytics.service.dispatchEvent
DolbyVision LL YCbCr 4:2:2
state.setIDRefDictionary
identity
Failed to unload %s - %s.
assertionInitialConnection
Timestamp:
Orientation type:
Found plugin %s.
com.apple.kext.load
Cancel 
Touch:
Network-Root
_MKEXTExecutable
_kmod_info
zlib deflate failed.
IOHIDConnection process:%@ pid:%d uuid:%@ caller:%@
Total Channels: %d Active Channels: %d\n
HIDPreferencesCopy
: 
%s %d - cannot allocate memory for target string
Can't load %s - no code for running kernel's architecture.
assertionActivityLog
AID
yes
TiltX:
MajorRadius:
ProbeScore
SupportsDownspread
Keyboard
Sticky Key Phase:
VendorID:
Can't read running kernel architecture.
DroppedEventMask
Underscan
IsPowerOn
/Library/DriverExtensions
URL = \"%@\", 
Created mkext for architecture %s containing %u kexts.
PerTaskAssertions
DeviceDescription
Link Command (with source)
DCI-P3 (Theater)
IOPMPowerSource
uuid
__IOHIDEventSystemRegister
Front Center
poweron
TCCAccessCheckAuditToken
AppleSmartBattery
SCPreferencesSetValue
SwipeRight 
Unknown CPU info given (type %d, subtype %d), using running kernel architecture %s.
Mkext checksum error.
FirstDroppedEventTime
AutoPowerOff Delay
initWithSession:
Can't load %s - dependency authentication problems.
USBDeviceCommand
Low Frequency Effects
eventtype
/System/Library/PowerEvents
GetReportCallback
user
 (from mkext)
AssertionOnBehalfOfPID
BT.709
virtualServices
ies
Product:
AutoTimesout
RGB 4:4:4
IOService:/
IOHIDEventSystemClientNotifyDispatchMach
__IOHIDEventSystemClientRefresh
_MKEXTBundlePath
DoIdrefScan
ServiceRecord
com.apple.kpi.private
Adding %s to mkext.
DCI-P3 (D65)
Hand
Events:
EstimatedAzimuth 
UTF32 Little Endian
com.apple.iokit.statenotification.name
Wake On LAN
 = 
LoginWindowProgress
QueueSize
IOHIDUserDevice State
vendorID
Vertical
UserVisible
IOHIDEventSystemClient.c
Dependencies have incorrect owner/permissions
Error encountered, unmapping executable file %s (offset %lu, %lu bytes).
unknown CPU architecture
Z:
assertion failure: Get report block already set
Can't update mod time of cache file %s - %s.
Started %s.
Personality %@ not found in %s.
MinLaneCount
com.apple.PowerManagement
Puck
PressedThreshold:
velocityDegreesPerSecond:
Failed to send personalities to the kernel.
IOHIDEventSystemConnection uuid:%@ pid:%d process:%@ type:%s entitlements:0x%x caller:%@ attributes:%@ state:0x%x events:%d mask:0x%llx dropped:%d dropStatus:%d droppedMask:0x%llx lastDroppedTime:%@
incompatible 
%-20.20s ERROR\n
assertionRelease
Process must be running as root to load kexts.
SampleInterval:
SupportsEnhancedMode
IONotificationPortSetImportanceReceiver
Unknown
HandTapHold
v16@?0^v8
onenessState
CurrentBrightness:
Can't load %s - failed to resolve dependencies.
Sticky Key Toggle:
IOParentMatch
setOutputEvent:
OSKextSetTargetString
Negotiating
Kext library recording diagnostics%s%s%s%s%s.
Personality Names
Video Timing
_IOPMCreatePowerOnDictionary received invalid date\n
eventQueue
IOHIDService name:%s id:0x%llx primaryUsagePage:0x%x primaryUsage:0x%x transport:%s locationID:%@ reportInterval:%d batchInterval:%d events:%d mask:0x%llx sensorcontrols:%d
droppedEvents
File access failure; can't open, or I/O error
48 Gbps (12Gbps/lane * 4 lanes)
Flags:
Statting %s for suffix.
Creating kext with path %s.
non
Front Center High
%@%s%s
ProcessName
Timing Attributes:\n
HIDPreferencesSetDomainForInstance
IOCircularQueueDescription
com.apple.system.powermanagement.prefschange
cancel
FEC:           %s\n
AppleUSBXHCI
DesktopModeAppliesOnBatteryPower
com.apple.hid.analytics.service
bg 
IOServicePublish
com.apple.private.hid.client.admin.internal
ChildEvents:
!hid_pthread_attr_init(&attribute, kIOHIDInterruptThreadPriority, kIOHIDInterruptThreadPolicy)
vendorUsagePage: %ld vendorUsage:%ld dataLength:%ld
s
Set Power
ReportInterval
Tap
Libraries declared for both com.apple.kernel and a com.apple.kernel.* component.
Link Rate:     %llu bps\n
array
options
SCDynamicStoreNotifyValue
assertion failure: Queue has already been activated/cancelled.
NormalizedForceVelocity:
connection_workloops
DEXT
IOCFUnserializeBinary
com.apple.system.accpowersources.timeremaining
suspended
should be %s
UnprotectLink
Physical Interconnect Location
workgroup_interval_force_enable
com.apple.private.hid.client.service-protected
64:27
EventType:
Unsupported mkext version 0x%x.
LocationID:
ColorModes
v16@?0r^v8
NaN
DeviceOpenedByEventSystem
_%s
IO
%@ -> %@ (kext is %@)
Compressed info dict from %u to %u bytes (%.2f%%).
BT.2020 (YCbCr)
kTCCServicePostEvent
File owner/permissions are incorrect (must be root:wheel, nonwritable by group/other)
__kernel__
com.apple.private.hid.client.admin
Traditional gamma (HDR)
MaintenanceImmediate
PressCount:
HandFlick
executable
assertions
Shoulder Button L2:
LatencyEventSystemOpen
HIDServiceAccessEntitlement
/System/Library/PrivateFrameworks/HIDPreferences.framework/HIDPreferences
NSPrincipalClass
Kext library setting simulated safe boot mode to %s.
Failed to open compression stream for %s - %s.
Symlink points outside of bundle.
Add Child
fd
ColorComponent0:
Key:
OSBundleSharedExecutableIdentifier
kernel
135:256
9:16
Stage:
Couldn't open CFBundle for %s.
%s - loaded dependency %s lacks valid OSBundleCompatibleVersion.
%s has no symtab in its executable (%s)
<dict>
PID
}\n
keyboardPress: %ld
.plist.gz
Calculated
Unprotected
Auto
DarkWakeBackgroundTasks
com.apple.iohidmanager.uuid
Direction Pad Up:
UserKeyMapping
.DS_Store
Link Training Data:\n\n
Pixel Clock:   %f Mhz (%u Hz)\n
%02x 
PSR:           %s\n
<string>typeID 0x%x not serializable</string>
BSD Name
RemoteActive
%s.%06d
FromEdgeTip 
eventMatching:forClient:
Internal error; overrun mapping executable file %s.
Get Loaded Kext Info By UUID
Data:
IOUSBDeviceDescription
UpdateLink
YCbCr 4:2:0
HeartRate
PropertyCache
OSBundleCPUType
com.apple.powermanagement.collectbt
Standard
/System/Library/HIDPlugins/SessionFilters
state.data
state.dictionaryIDRefDictionary
wake
assertion failure: Device already scheduled
Relative
Failed to remove identifier->path cache %s - %s.
9 Gbps (3Gbps/lane * 3 lanes)
ColorComponent2:
BrightnessChanged:
ServiceRecords
Kext library architecture is %s (unchanged).
IOHIDServiceFilter uuid:%@ name:%@ %@
Remove Child
Encrypted
SystemPowerSettings
FastSwipe 
EventTime
Couldn't read resource file %s.
HIDAnalyticsEventActivate
%s.%02X%02X%02X%02X-%02X%02X-%02X%02X-%02X%02X-%02X%02X%02X%02X%02X%02X
Peak 
Open
Kext identifier->path cache - kext info is not an array.
ProtectLink
16:9
TPS2
(date object)\n
<off> 
Usage:
%s%s
Link Mode:    %s\n
AppleLSIFusionFC
SymbolicHotKey
Thumbstick Button Left:
LocationID
Warnings
Unable to get data to create cache file %s.
UpstreamFormat
AdobeYCC601
IOAccessoryIDBusBulkDataEndpoint
AuxiliaryPressure:
10:16
Failed to close compression stream for %s - %s.
Reading resource %s.
EAC3
Locked
HIDKeyboardModifierMappingPairs
/System/Library/HIDPlugins/ServiceFilters
/AppleInternal/Library/HIDPlugins/ServicePlugins
%s Element\n
%-20.20s %d\n
boolean, <true/> or <false/>
Limited
CFBundleIdentifier and CFBundleVersion must be < 64 characters.
begin
Shoulder Button R2:
/System/Library/HIDPlugins/ServicePlugins
Disk Sleep Timer
Compass
assertion failure: Set report block already set
Executable file doesn't contain kernel extension code (no kmod_info symbol or bad Mach-O layout).
Bad mkext magic/signature.
+
Date of first use
Mask:
caller
ClientRecords
OSBundleDebugLevel
com.apple.private.hid.client.event-dispatch.internal
LongPress
Force
GameController
resetCount
com.apple.hid.queueUsage
Root
IOCFSerializeBinary
YES
copyEvent:matching:options:
/usr/appleinternal/lib/HIDPlugins
HIDAnalyticsEventSetStringValueForField
IOHIDActivityUserIdle
<IOHIDEventSystem %p [%p]>{\n\tserviceDict=%@ \n\tnotificationDict=%@ \n\tmatchNotifySet=%@ \n\tclientSet=%@}
LatencyCopyEvent
Dependency lacks appropriate value for OSBundleRequired and may not be available during early boot
%s (version %s): is%s started.
Upstream
DP
IOKit.framework:IONotificationPortGetRunLoopSource bad CFMachPort, %s\n
SCPreferencesCommitChanges
%s has multiply defined %ld symbol%s
>
Loaded kext info:\n%s
SwipeDown 
Ended
Watch
DisplayIntegrated
The booter does not recognize symbolic links; confirm these files/directories aren't needed for startup
Serial
batteryCycleCountData
FromEdgeFlat 
tcc_authorization_check_audit_token
Description
BoundaryScroll
services
Cache file %@ - owner not root; not using.
Send Resource
IOMatchCategory
DTS
Dolby Atmos (MAT2.1)
HIDCapsLockLEDOn
Tap Count:
kern_result == KERN_SUCCESS
%s is invalid; can't resolve dependencies.
com.apple.kpi.kcov
/Library/Caches/com.apple.xbs/CB3C5685-5D2F-4785-B125-00238CC55C5B/TemporaryDirectory.w7GqJC/Sources/IOAVFamily_user/IOAV.cpp
HumanReadableReason
Info dictionary property value is of illegal type
HIDServiceFilter
IORequiredPacketFilters
Failed to read XML from mkext: %s.
Direction Pad Down:
Could not get absolute path of kext!
%s - internal overrun in executable file (%s).
Running kernel architecture is %s.
SetReportCnt
Kext Request Predicate
Reading kext UUID for Address\n.
com.apple.kpi.dsep
com.apple.iokit.IOServiceAuthorizeAgent
CH2:
Rear Right
Source
\"
Phase:
LastDroppedEventTime
Dolby TrueHD (MAT2.1)
IOAVVideoColorBitsPerPixel
Can't create kext: missing or non-string path in identifier cache entry %d.
Temp cache file name too long: %s.
HDCP1
powerInfoPrecise
OSBundleRequired not set
AllowMultipleCreates
256:135
service.carplay
OSBundleCPUSubtype
com.apple.private.hid.client.motion-event-privileged
TimeoutActionTurnOff
TPS4
<
PresentActive
SLCheckInCapability
IOHIDEventSystemClientIsUnresponsive
setHIDEventService:
LatencyCopyProperty
Kext %s-space log filter changed from 0x%x to 0x%x.
Removing identifier->path cache %s.
Continuous
Validation Failures
setting load address of %s to 0x%0llx
Command
Supported Features
time of last save
Info dictionary property value is illegal
Couldn't read resource URL in %s for resource %s.
_kasan
HIDPreferencesSynchronizeForInstance
com.apple.iokit.statenotification.set
kernelEventQueue
Safe Boot
ReprotectLink
IOHIDSystem
IOGeneralInterest
v28@?0Q8^{dispatch_mach_msg_s=}16i24
Decompress-only
:
SwipeLocked 
 validation
/AppleInternal/Library/HIDPlugins/ServiceFilters
%dx%d%c %.3f Hz, %dbpc %s Range %s, %s colorimetry, %s EOTF
Bottom Button M1:
SecTaskGetCodeSignStatus
activity
EstimatedAltitude 
Confidence:
zlib inflateInit failed.
%s is a kernel component with no dependencies.
HIDActivityState
BundlePath
com.apple.system.accpowersources.source
IOHIDService - RunLoopCompatibilityThread
IOHIDDeviceDispatchMach
Can't create kext: missing or non-string CFBundleIdentifier in identifier cache entry %d.
HIDPreferencesCopyDomainForInstance
Kext claims a shared executable with named kext, but that kext can't be found
dis
CoreDisplayProgress
OSBundleLoadAddress
%s does not declare a kernel dependency; using %s.
IOUSBDeviceDescription: pid/vid/ver=%04x/%04x/%d class/sub/prot=%d/%d/%d Mfg:%@ Prod:%@ Ser:%@\n%@
/System/Library/Caches/com.apple.kext.caches
.iohid
CapsLockDelayOverride
v12@?0i8
Velocity
%s (version %s%s%s): same version, different UUID (%s) is loaded.
%s:\n
TiltY:
IOKitLib.c
OSKextIdentifierCacheVersion
Resolving dependencies for %s.
Failed to remove temp cache file %s - %s.
Flushing dependencies for all kexts.
MotionActivity
%lld 
unknown
StandardType:
AssertionOnBehalfOfBundleID
/System/Library/Frameworks/Security.framework/Security
IOClass
lastNotifyEventTimeStamp
Failed to read loaded kext info from kernel - %s.
/System/Library/PrivateFrameworks/TCC.framework/TCC
PrimaryUsagePage
Embedded
%-25.25s %d\n
AspectRatio
Traditional gamma (SDR)
(unknown object)\n
port
Kexts may not link against com.apple.kernel; use either com.apple.kpi.* libraries (recommended), or com.apple.kernel.* (for compatiblity with older releases).
Nameless (via IOPMAssertionCreate)
kern.waketime
Opening CFBundle for %s.
Direction Pad Right:
TCCService
SetReportCallback
Executable kext %s with no dependencies?!
<IOHIDConnectionFilterRef:%@>
False
/usr/appleinternal/lib/HIDPlugins/ConnectionPlugins
Front Right Center
HIDPreferencesCopyMultiple
assertionActiveAsyncByProcess
HIDAnalyticsEventSetIntegerValueForField
OneBitAudio
^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}16@?0^{os_state_hints_s=I*II}8
ClickCount:
Requesting start of %s.
Reading loaded kext info from kernel.
OSBundleLoadSize
FIXME: IOCFSerialize has detected a string that can not be converted to UTF-8, \"%s\"
IOPower:/IOPowerConnection/IOPMrootDomain
FromCorner 
Tap 
Invalid
DriverKit
<integer>
trace
%-20.20s 0x%016llX\n
%s - dependency '%s' not found.
IOBatteryInfo
SCPreferencesGetValue
IOHIDManagerStateQueue
OSBundlePrelinked
<true/>
CPUPower
Some dependencies are causing circular references
Failed to serialize data for cache %s.
Start Exclude Level
Mkext plist has no kexts.
Video Link Data:\n\n
Failed to check path %s (CF error %ld).
<array>
filterSetProperty:forKey:forClient:
Orientation usage:
Info dictionary missing required property/value
CP2520 Pattern 3
com.apple.
disk 
HighFrequency
%s found link dependency %s.
ForceOffBusEnable
HIDAnalyticsEventCreate
Can't serialize personalities.
%-20.20s True\n
com.apple.private.hid.client.debug-tool
(missing)
EventTypeCounts
AssertLevel
IOHIDDevice
leeway
Cache file %@ is not a regular file; ignoring.
Failed to open CFBundle for %s.
Releasing CFBundle for %s
4:3
shutdown
IOUSBHostDevice
Range 
KEXT
AtmosphericPressure
IdleNotificationTime
Personality has no CFBundleIdentifier; the kext's identifier will be inserted when sending to the IOCatalogue
Get All Load Requests
DSC:          NO\n
Audio Link Data:\n
IOClassNameOverride
SystemSleepPreventersWithID
IOHIDDeviceSuspend
Third-party Driver Extensions are ineligible to run in Safe Boot, or match on devices during early boot. Please remove the OSBundleRequired key from your Info.plist.
Failed to lookup uuid with address from kernel - %s.
Minor
DidStartLink
GRGB Tunneled as YCbCr422 (Even line blue)
NONE
PowerNap
NavigationSwipe
Y:
UTF16 Big Endian
Swipe
Internal error converting URL
createPowerSource returned 0x%x\n
B24@?0r*8^v16
com.apple.powerd.assertionpolicy
com.apple.system.powermanagement.useractivity2
Rx:
eventCount
eventMask
com.apple.kpi.
com.apple.iohideventsystem
%s - Interface kext must have exactly one dependency.
IOAVVideoInterface
SetDeviceDescription
DTSHD
Manufacturer
Start 
<IOHIDNotificationRef %p (ref:%d xref:%d), flags:%x  %p,%p,%p,%p,%p,%p>
dext
BT.2100 HLG
set
Carrier Mode Low Voltage
CH1:
internal error
SystemPowerProfileOverrideDict
DataLength:
Dependencies aren't loadable during safe boot
Fast:          %s\n
com.apple.system.accpowersources.attach
Can't get info dictionary for %s.
Shoulder Button R1:
NormalizedForce:
IOHIDFamily
LastEventTime
Note: OSKextCopyKextsWithIdentifiers() - identifier %s not found.
/System/Library/HIDPlugins
userActivityTimeout
GenerationCount:
Sending named personalities of %s to the kernel:
DPCP
SubType:
CFBundleIdentifierKernel
zlib deflateInit failed.
DMT
getTagString
head
 (with termnation of IOServices)
HIDPropertiesRequiredForMatching
Can't create kext from cache: %s is already open and has a different CFBundleIdentifier from identifier->path cache entry %d.
LegacyBatteryInfo
gamingEnergyMode
Layout:\n
PowerSource
)\n
Biometric
%p%p%p%p
isVirtualService
OSKernelCPUSubtype
<!-- 🤦 -->
IOHIDQueue
OSBundleEnableKextLogging
 (expected while realizing)
AsyncClientAssertionId
NTSC
sizeof(IOCircularDataQueueDescription) == inband_outputCnt
ClearTime
Identity 
SwipePending 
<OSKext %p [%p]> { 
HIDMouseScrollAcceleration
ShipChargeLimitEnabled
AssertType
%s: %lld.%0*lld\n
Dolby Atmos (EAC3 7.1)
original URL = \"%@\", 
Swing Voltage: %d\n
HIDAnalyticsEventCancel
32 Gbps (8Gbps/lane * 4 lanes)
chargeSocLimitNoChargeToFull
Can't create kext: path in identifier cache entry %d doesn't name a kext.
Can't determine real path for %s (%s)
com.apple.backboardd.hid
Manufacturer:
IODPService
Video
CP2520 Pattern 1
ups
Altitude:
integer
UserActivityLevels
NotificationActive
%s.IOHIDManagerRef
elementSetTime
Connections
OSKextIdentifierCacheKextInfo
AssertStartWhen
VAC-T
serviceNotification:added:
Requesting stop of %s.
Channel %d: %s\n
Audio
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n
Adding CFBundleIdentifier %s to %s personality %s.
CollectionCookie
Kernel error handling kext request - %s.
assertionWasCoalesced
Dolby Atmos (EAC3)
%@%@
HIDPointerAcceleration
DownstreamFormat
HIDClickSpace
v24@?0Q8Q16
Type:
Encoding:
Depth: [%d bpc] Encoding: [%s] Range: [%s] Colorimetry: [%s] EOTF: [%s] DSC: [%s]\n
Proximity
PropertyMerge
invalid pixel encoding
/System/Library/AppleUSBDevice/USBDeviceConfiguration.plist
RetrainLink
state.stringIDRefDictionary
</%s>
MatchingEvent
Revision
Front Right High
Wake On Clamshell Open
Begin
Indirect dependencies can't be resolved
PrimaryUsagePage:
SleepServices
CalibrationDeadZoneMin
none
%c[0m
LiftOffPredicted 
Kext identifier->path cache for %s - base path missing or invalid.
name
HardwareAddress
_MKEXTInfoDictionaries
/
Identity:
Resting 
LowSNRSwipe 
aud 
push 
Transition: None
LogLevel
msgCount
(kernel) %s
True
CP2520 Pattern 2
Architecture %s not found by name, using running kernel architecture %s.
OSBundleRequiredPromotion
 (kernel component)
SCDynamicStoreSetNotificationKeys
ended
HIDServiceSupport
com.apple.iohideventsystem.available
keeping
com.apple.private.hid.client.event-monitor.internal
assertionActivityUpdateProcessList
All
\n
com.apple.iohid
Failed to remove personalities of %s from IOCatalogue - %s.
%s has no info dictionary; can't resolve dependencies.
%u
IOHIDEventSystemClient
PropertyNotificationCount
assertionAsyncOffloadDelay
assertionActivityUpdateData
IODPHDMIControllerPort
AutoPowerOff
CalibrationMin
UserInterfaceSupported
OSBundleCompatibleVersion
DoCFSerialize
Hibernation
LED
CASecureLayerOnScreen
Rate:
CtrlKeyboardUsageMap
%s: %s - no such file or directory.
plugin
tail
Kext Request Result Code
(executable from mkext)
DST
batteryChargingIconoGraphy
HIDConnectionPlugin
 ->
ColorComponent1:
Only Apple kexts may link against com.apple.kpi.private.
Startup
Error uncompressing kext cache file %s - zlib returned %d - %s.
Validating %s.
SleepDisplay
Can't serialize personalities for %s.
No Description
BuiltIn:
Motion:
%-20.20s %qd\n
Intermediate
setPowerSourceDetails returned 0x%x\n
userdevice
CFBundlePackageType is DEXT and bundle declares CFBundleExecutable; use only one.
Kext has no executable or compatible version, so it should not declare any OSBundleLibraries.
 off
Standby Delay
CoreGraphicsProgress
%-20.20s %s\n
com.apple.kpi.kasan
%s has no Info.plist file.
%-20.20s\n
Generation:
AssertReleaseWhen
IODPDevice
Pre-emphasis:  %d\n
Audio Channel Layout Data:\n\n
CEA
AutoPowerOff Enabled
DestroyFVKeyOnStandby
SCPreferencesRemoveValue
devices
Bottom Button M2:
%s - dependencies already resolved.
Can't read info dictionary for %s: %s.
CreatorBacktrace
com.apple.kernel
Rear Left
On
IsVirtual
<%s %s>
category < kIOHIDLogCategoryCount
NextThreshold:
(unknown)
DeepSleep
Undefined
.
phase:
promotable 
ForcePending 
 dependencies
/System/Library/PrivateFrameworks/HIDAnalytics.framework/HIDAnalytics
Level:
ActivityLog
%s/%s%@/%@%s%s%s
IOAVService
Sleep On Power Button
TransducerIndex:
NormalizedPositionDeltaY:
Rate Controlled
Personality CFBundleIdentifier names a kext that can't be found
Can't create kext: invalid CFBundleVersion in identifier cache entry entry %d.
Console
Face Button B:
Decompress|Passthrough
kIOHIDServerConnectionRootQueue = hid_dispatch_pthread_root_queue_create(\"IOHIDEvent Server Connection - Root\", &attribute, NULL, 2)
com.apple.kext.unload
VendorID
hid-workgroup-interval
Reading requests from kernel.
Inhibit
PackID
PerformanceWarning
Downspread:    %s\n
%s:\n\n
None
HIDParameters
IOKit Power Source Copy
dominoState
Cancelled
Deprecated property (ignored)
%c[1m
matchService:options:score:
%@:
openOptions
A system kext has a property set that it shouldn't
Reading list of all kexts requested by kernel since startup.
15:9
Services
Releasing CFBundle for %s.
OSBundleLibraries
SetPower
<%s ID=\"%d\">
alloc
connection
GestureType:
BT.2020 (RGB)
TrainLink
IOHIDEvent Interrupt - Root
64-bit kexts must use com.apple.kpi.* libraries, not com.apple.kernel* libraries.
__unknown__
com.apple.private.hid.client.service-protected.internal
com.apple.private.hid.client.debug-tool.internal
PowerRelativeToShutdown
CalibrationMax
UTF8
Slave
v8@?0
SCDynamicStoreSetValue
Count:
Filters
0x%llx
with
filterEvent:toConnection:fromService:
%s has no executable for architecture %s.
DolbyVision VSVDB
Automatic Restart On Power Connect
Hibernate Free Time
Shoulder Button L1:
%-20.20s %dx\n
Display Sleep Timer
com.apple.private.hid.client.event-filter.internal
Automatic Restart On Power Loss
Length
No kexts found for these libraries
Battery Power
UPS Power
IOHIDSessionFilter
CH0:
%s:%@
CEAShortID
WillStopLink
3:4
Rz:
filterEvent:
Gyro
Progress:
ValidPixelEncodings
Front Left
IOHIDSessionFilterRef uuid:%@ name:%@ %@
Kext Request Info Keys
assertionCreate
Default RGB
AC Power
returnCode
SCPreferencesCreateWithAuthorization
HIDRMHash
VendorDefined
IONetworkInterface
/System/Library/DriverExtensions
------------------------\n
Bottom Button M3:
isOpen
%s: %s + %lu
Can't stat path %s - %s.
Compressed write error for cache file %s - %s.
sYCC601
%s.IOHIDDeviceRef:0x%llx
%s.IOHIDQueueRef
IOHIDSession - SessionEventDispatch
Checking CFBundle of %s for executable URL.
Kext Request Arguments
PrepareLink
Downstream
RequestTerminate
Standby Battery Threshold
TCCAccessPreflight
.ioplist.gz
Reading cache file %s.
OSBundleDependencies
adapterDetails
batteryGaugingMitigationAction
Quality:
Flavor:
scheduledby
%-20.20s %s (%d)\n
TimeoutTimeStamp
cpu 
ProximityWake
IOHIDQueueDispatchMach
Orientation
OSBundleWiredSize
Can't get executable for %s (architecture %s).
dict
Joystick Axis Z:
OSKEXT_BUILD_DATE 16:20:56 Oct  3 2026
Can't create kext cache under %s - group not wheel.
Get Kernel Requests
%s adding implicit KASan dependency
Realpath for %s is %s
Failed to get %s for portType=%d, portNumber=%d, portVariant=%d\n
loaded 
%s: 
MultiAxisPointer
Bundle URL unexpectedly NULL!
.kext/
MaxInputReportSize
HIDServicePlugin
6.0
IOAccessoryIDBusBulkData
TimeoutSeconds
xvYCC601
Hibernate Mode
setProperty:forKey:
plist
Extra Button R4:
 warnings
NULL
com.apple.hid.analytics.event-system
IOHIDEventSystemClient State
Clearing \"has all dependencies\" for %s.
Can't load %s - ineligible during safe boot.
IOAVDisplayMemory
<%s>
UTF32 Big Endian
Terminate IOServices
Can't read mkext fat header.
Off
SampleInterval
Down
ThermalWarning
Kexts with a kernel library < v6.0 must set MODULE_VERSION the same as CFBundleVersion to load on kernel < v6.0.
GoOffAndOnBus
USBDeviceCommandParameter
PM Notifications
%-20.20s %llu us\n
HDCP
IOHIDEventSystem.c
version
Dolby TrueHD (MAT2.0)
assertion failure: Client has already been activated/cancelled.
Can't read plist from cache file %s - %s.
SystemTimeOutExpired
%-20.20s %08x\n
Density:
%s - missing load info or dependencies array in applier function.
Type
Kext was not created from an URL and can't be authenticated
Can't create CFWriteStream to save cache %s.
MaxChannelCount
MPEG
%x, %lx, 0x%llx, 0x%llx\n
UsagePage:
Cache file %@ - wrong permissions (%#o, should be %#o); not using.
Can't read loaded kext info - current architecture %s != kernel's architecture %s.
OSKernelResource
%s: internal overrun (%p, string_index: %d, file_end: %p) in executable file (%s).
IsDeviceUsable
IdleSleepPreventersWithID
ClickDownPredicted 
Kext identifier->path cache for %s - not a dictionary.
%s:%u: %s(): %s
 
Sleep
SCDynamicStoreCopyMultiple
ReportDescriptor
Failed to uncompress %s%s from %s.
ID
productID
HIDAnalyticsEventAddField
data
%-20.20s %u\n
LastActivityTimestamp
 failed
Action
DolbyVision LL RGB 4:4:4
IOCFUnserialize: %s near line %d
IODeviceTree
Button
YCbCr 4:2:2 (DP tunneling)
IODPPort
ServiceEntitlements
 (dependencies not fully resolved) ->
StandardType
buttonState: %ld
-----------------------------------------------------------------------\n
Bottom Button M4:
setEventDispatcher:
Can't create kext from cache: %s is already open and has a different CFBundleVersion from identifier->path cache entry %d.
EventSystemEntitlements
Face Button Y:
IOHIDUserDeviceStateQueue
ClientSuspend
IONameMatch
batteryShippingChargeLimit
X:
id
Kext contains symlink at %s which points outside of its bundle at %s; rejecting.
activate
batteryShippingChargeLimitState
%-20.20s 0x%08x\n
IOServiceFirstMatch
Translation
%s found %s%s%sdependency %s for %s%s.
Successfully loaded %s.
&amp;
State:
allocator
GlobalUniqueID
hidsignpost
IOUSBHostInterface
Mapped executable file %s (offset %lu, %lu bytes).
Loaded kext info from kernel is wrong type.
UnsafeColorElementIDs
EventLog
HIDDefaultSensorControlOptions
TurnedOn
MaxLaneCount
, DSC (%f bpp, decompress)
sleep
Trying to authenticate kext with no authentication function, failing.
%s, version %s is already in the identifier lookup dictionary at index %d.
MPEG1
Established
IOAccessoryBulkDataEndpoint
ActivityState
Protection Command
Master
xvYCC709
Enabled
Kexts found for these libraries lack valid OSBundleCompatibleVersion
timeout
HIDKind
%@#%@
TargetBrightness:
Major
Azimuth:
Not running as root; skipping save of identifier->path cache.
Usage
ForceOffBusDisable
no
!pthread_create(&__serviceRunLoop.thread, &attribute,(ThreadRoutine)&__IOHIDServiceRunLoopCompatibilityThread, NULL)
OSKernelCPUType
Sending %d personalit%s to the kernel.
*
Extended
Properties
Virtual:
memory exhausted
Extracting %s%s from %s.
PowerOnImmediate
HIDScrollAcceleration
Personality CFBundleIdentifier differs from containing kext's (not necessarily a mistake, but rarely done)
mkext URL = \"%@\", 
Direction Pad Left:
BatchInterval:
DolbyVision LL YCbCr 4:2:2 (DP tunneling)
WakeImmediate
Began
ResourcesUsed
Rear Left Center
scRGBfixed
Name
v24@?0r^v8r^v16
Saving cache file %s.
com.apple.private.hid.client.motion-event-privileged.internal
YCbCr 4:2:2
 %@=%d
Can't open CFBundle for %s.
IOKitDebug
IOPacketFilters
dominoMainDisplay
???
Sending all personalties for %s to the kernel.
assertionFeatureSupported
Test Mode:    %d\n
IOHIDEvent
1.2.12
Invalid cache format %d specified.
IODPController
SetDevicePreferredConfiguration
Front Left Wide
key
com.apple.system.powermanagement.SystemLoadAdvisory
_
Key
StreamSampleRate
IOMIGMachPort
OSBundleIsInterface
(\n
VendorIDSource
OSBundleUsesAbsolutePath
size
Power Management power source queue
Authentication Failures
IsCoalesced
CalibrationDeadZoneMax
ProductID
%-20.20s %ld\n
Start Matching Exclude Level
Mkext plist full size is %u.
Link ID:      %u\n
LowPowerMode
LatencySetProperty
; reinitializing all kexts for new architecture
Recorded %s%s, id %s, version %s.
NoIdleSleepAssertion
UnifiedSleepSliderPref
UTF16 Little Endian
MechanicalAngleDegrees:
hideventsystemclient.default.queue
Failed to open CFBundle (unknown error).
y
IOAVController
HIDAnalyticsHistogramEventCreate
High Standby Delay
%-20.20s %-8llu %-8llu %-8llu %-8llu %-8llu\n
Kext library %s using caches.
OSBundleRetainCount
DVI
24 Gbps (6Gbps/lane * 4 lanes)
HID - IOService Enumeration
userEventQueue
OSKextVariantOverride
com.apple.iokit.powerdxpc
%@#%04lx#%04lx#%016lx#%ld
HIDMouseAcceleration
HIDPreferencesSetDomain
0x%qx
IODeviceTree:
IOPropertyMatch
assertionCopyActivityUpdate
BT.2020 (YcCbcCrc)
Sink
Kernel request call returned no data.
Pointer
SwipeUp 
Normal
dispatchQueue
Failed to create kext request.
MaxLinkRate
0 Gbps (FRL disabled)
Closed
The 'CFBundleIdentifierKernel' key is required in your personality to specify the base kext to load when your kext is instantiated.
%s does not contain code for architecture %s.
/Library/Apple/System/Library/HIDPlugins/SessionFilters
IOPMSleepFailure
ValueType:
PressCount
Rejecting invalid/inauthentic kext for bundle id %@ at location %@.
HIDPreferencesCopyForInstance
System Sleep Timer
compatible 
Horizontal
batteryChargingIconoGraphyAction
setBatteryDofu
Up
Not saving %s - read-only filesystem.
Error initializing zlib uncompression for %s.
<data>
EventFilterMask
/System/Library/HIDPlugins/ConnectionPlugins
batteryGaugingMitigation
CalibrationSaturationMin
assertion failure: CFMachPortCreateWithPort
kTCCServiceListenEvent
_kTCCAccessRequestOptionSyncCallback
CalibrationSaturationMax
Zoom
workgroup_interval_force_disable
ProtectedAccess
queueType
IOUserEthernetInterfaceMergeProperties
queueHeaderShadow->allocMemSize == map_size
SCDynamicStoreCreateRunLoopSource
MaxEventLatency
Can't load %s - authentication problems.
<string>
activityStateChangeCount
%g kHz %dch %d-bit %s
deviceProtocol
Can't load %s - failed to resolve dependencies based on loaded kexts.
Dolby TrueHD (MAT1.0)
EventMask:
%02x%s
Can't load %s - dependencies ineligible during safe boot.
com.apple.private.hid.client.event-monitor
Behavior:
Get Kext UUID by Address
Scanning %s for kexts.
configurations
LinearPCM
TCPKeepAlivePref
IOHIDResource
Directories
a
Location
restart
en
40 Gbps (10Gbps/lane * 4 lanes)
b
CountryCode
DisplayWake
QueueCallbackTimestamp
Can't unserialize kext request response: %s
Mkext length field %d does not match mkext actual size %d.
SLCheckIn
Absolute
KextIdentifiers
Split:         %s\n
batteryHeatMapData
createOptions
Number:
Joystick Axis Y:
0x0
com.apple.PowerManagement.control
%s%@%s
DisplayIntegrated:
IOUSBDeviceData
Compressed executable from %u to %u bytes (%.2f%%).
Horizontal:    Total: %5u Active: %5u FrontPorch: %4u SyncWidth: %3u BackPorch: %3u SyncPolarity: %u PixelRepetition: %u SyncRate: %10.6f kHz\n
Product Description
%s: %s\n
manufacturerString
Rotation
Kext identifier->path cache for %s - version %d unsupported.
AssertPID
_IOHIDLogCategory
Finger
assertionUpdateActivity
LastActivityTime
8.0.0b1
HIDSessionFilter
(data object)\n
com.apple.powermanagement.sleepservices
Kext declares no com.apple.kpi.* libraries; if it references any kernel symbols, it may fail to link.
%s not in base path %s for identifier->path cache - marking.
For loaded kext %s, v%s: no opened kext matches.
Lane Count:    %d\n
Flushing load info for %s (%s dependencies)
%s already has dependencies resolved.
filterEventMatching:event:forClient:
<integer> (kexts may not use <real>)
DeviceUsage:
TimeoutAction
Vertical:      Total: %5u Active: %5u FrontPorch: %4u SyncWidth: %3u BackPorch: %3u SyncPolarity: %u PixelRepetition: %u SyncRate: %10.6f Hz\n
DefaultConfiguration
DarkWake
v48@?0^v8^v16^v24^v32^v40
Flushing load info for all kexts (%s dependencies)
%s - loaded dependency %s, v%s is not compatible with requested version %s.
/AppleInternal/Library/HIDPlugins/SessionFilters
Kexts should declare dependencies on either com.apple.kernel* or com.apple.kpi.* libraries, not both.
Can't load %s - dependencies ineligible during safe boot:\n%@
```
