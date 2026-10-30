# `/System/Library/PrivateFrameworks/IsolatedCoreAudioClient.framework/IsolatedCoreAudioClient`

iOS 27.2 dyld shared cache image. Version `7.49.200.0.0`. **[DSC]**

## Linked libraries (12)

- `/System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam`
- `/System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking`
- `/usr/lib/libbsm.0.dylib`
- `/System/Library/PrivateFrameworks/CoreAudioOrchestration.framework/CoreAudioOrchestration`
- `/System/Library/PrivateFrameworks/caulk.framework/caulk`
- `/System/Library/Frameworks/CoreAudio.framework/CoreAudio`
- `/usr/lib/libMobileGestalt.dylib`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libc++.1.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 10 classes, 7 protocols, 138 methods, 30 properties

### Class pages

Every class and protocol, with its methods: [`IOThreadXPCMappedMemoryTransporter`](../objc/IOThreadXPCMappedMemoryTransporter_IsolatedCoreAudioClient.md), [`IOThreadXPCSemaphoreTransporter`](../objc/IOThreadXPCSemaphoreTransporter_IsolatedCoreAudioClient.md), [`IOThreadXPCWorkgroupTransporter`](../objc/IOThreadXPCWorkgroupTransporter_IsolatedCoreAudioClient.md), [`IsolatedCoreAudioClientNSXPCListenerDelegate`](../objc/IsolatedCoreAudioClientNSXPCListenerDelegate_IsolatedCoreAudioClient.md), [`IsolatedCoreAudioReverseSiphonProtocol`](../objc/IsolatedCoreAudioReverseSiphonProtocol_IsolatedCoreAudioClient.protocol.md), [`IsolatedCoreAudioServerProtocol`](../objc/IsolatedCoreAudioServerProtocol_IsolatedCoreAudioClient.protocol.md), [`IsolatedCoreAudioSiphonProtocol`](../objc/IsolatedCoreAudioSiphonProtocol_IsolatedCoreAudioClient.protocol.md), [`IsolatedCoreAudioUseCaseConnection`](../objc/IsolatedCoreAudioUseCaseConnection_IsolatedCoreAudioClient.md), [`IsolatedCoreAudioXPCService`](../objc/IsolatedCoreAudioXPCService_IsolatedCoreAudioClient.md), [`IsolatedCoreAudioXPCSiphon`](../objc/IsolatedCoreAudioXPCSiphon_IsolatedCoreAudioClient.md), [`NSCoding`](../objc/NSCoding_IsolatedCoreAudioClient.protocol.md), [`NSObject`](../objc/NSObject_IsolatedCoreAudioClient.protocol.md), [`NSSecureCoding`](../objc/NSSecureCoding_IsolatedCoreAudioClient.protocol.md), [`NSXPCListenerDelegate`](../objc/NSXPCListenerDelegate_IsolatedCoreAudioClient.protocol.md), [`ReverseSiphonDelegate`](../objc/ReverseSiphonDelegate_IsolatedCoreAudioClient.md), [`TraceManager`](../objc/TraceManager_IsolatedCoreAudioClient.md)

### Classes

`IOThreadXPCMappedMemoryTransporter`, `IOThreadXPCSemaphoreTransporter`, `IOThreadXPCWorkgroupTransporter`, `IsolatedCoreAudioClientNSXPCListenerDelegate`, `IsolatedCoreAudioUseCaseConnection`, `IsolatedCoreAudioXPCService`, `IsolatedCoreAudioXPCSiphon`, `NSXPCConnection`, `ReverseSiphonDelegate`, `TraceManager`

### Protocols

`IsolatedCoreAudioReverseSiphonProtocol`, `IsolatedCoreAudioServerProtocol`, `IsolatedCoreAudioSiphonProtocol`, `NSCoding`, `NSObject`, `NSSecureCoding`, `NSXPCListenerDelegate`

### Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (class, TB,R) supportsSecureCoding;
@property (T@"NSObject<OS_xpc_object>",&,N,V_serverMemory) serverMemory;
@property (T@"NSObject<OS_xpc_object>",&,N,V_clientListenableSemaphore) clientListenableSemaphore;
@property (T@"NSObject<OS_xpc_object>",&,N,V_clientPingableSemaphore) clientPingableSemaphore;
@property (T@"NSObject<OS_xpc_object>",&,N,V_workgroup) workgroup;
@property (T@"NSXPCInterface",&,N,V_mInterface) mInterface;
@property (T@"NSString",C,N,V_mEntitlementString) mEntitlementString;
@property (T@"NSMutableDictionary",&,N,V_mConnections) mConnections;
@property (T{function<void (int)>={__value_func<void (int)>=(type=[24C])^v}},N,V_mClientReaper) mClientReaper;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSXPCConnection",&,N,V_connection) connection;
@property (Ti,N,V_pid) pid;
@property (TI,N,VuseCaseID) useCaseID;
@property (T{shared_ptr<ServerSideAudioSwitchboard>=^{ServerSideAudioSwitchboard}^{__shared_weak_count}},N,V_mServerSideSwitchboard) mServerSideSwitchboard;
@property (T{shared_ptr<IsolatedCoreAudioSiphon>=^{IsolatedCoreAudioSiphon}^{__shared_weak_count}},N,V_mSiphon) mSiphon;
@property (T{shared_ptr<SiphonClientMap>=^{SiphonClientMap}^{__shared_weak_count}},N,V_mClientMap) mClientMap;
@property (T@"NSMutableSet",&,N,V_reverseConnections) reverseConnections;
@property (T@"NSXPCListener",&,N,V_reverseListener) reverseListener;
@property (T@"NSXPCInterface",&,N,V_reverseInterface) reverseInterface;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Strings (258)

```
IsolatedCoreAudioClientExclaveKitProxy.cpp
basic_string
ClientSideAudioSwitchboardIOThread.mm
yyyy-MM-dd_HH-mm-ss
ICAC_Allow_FerryError_Spindump
ReverseSiphonDelegate.mm
com.apple.coreaudio
IsolatedCoreAudioClientExclaveKitProxy_FerryError_
No-Op Client IO Thread
HALUseCase.cpp
/usr/local/lib/libtailspin.dylib
%s
IsolatedCoreAudioServer
TB_FATAL: invalid value: unexpected case value, %llx
IOThreadXPCMappedMemoryTransporter
success
tailspin_config_create_with_default_config
tailspin_dump_output_with_options_sync
AudioHAL
com.apple.audio.isolated.client.service
Client Side IO Thread
ClientLocalServer Workgroup
SiphonIOClient.cpp
This object may only be decoded by an NSXPCCoder.
hasValidLocalIOThread: 
receivedPingFromLocalClientThread: 
IOThreadXPCSemaphoreTransporterClientListenable
IsolatedCoreAudioClientWorkgroup.mm
IsolatedCoreAudioXPCService.mm
unordered_map::at: key not found
AudioAvailabilityApparatus.cpp
AudioClientInstance.cpp
TraceManager.mm
AudioHAL_%@_%@.tailspin
tailspin_oncore_sampling_period_set
XPCConnectionToServer.mm
serverThreadStarted: 
IsolatedCoreAudioSiphon
TSPDumpOptions_CollectOsLogs
tailspin_buffer_size_set
tailspin_dump_output_with_options
IOThread.cpp
IsolatedCoreAudioClientBaseNSXPCConnection.mm
IsolatedCoreAudioServiceLauncher.mm
com.apple.private.isolated.audio.coreaudioclient
IsolatedCoreAudioXPCSiphon.mm
failure
/tailspins
/usr/lib/libtailspin.dylib
TSPDumpOptions_CollectAriadnePlists
ServerSideHardware.cpp
v16@?0@\"IOThreadXPCWorkgroupTransporter\"8
RemoteAudioHardwareServer.mm
hasValidResources: 
i
-
TSPDumpOptions_CollectOsSignposts
tailspin_config_apply_sync
IsolatedCoreAudioClientNSXPCListenerDelegate.mm
IOThreadXPCSemaphoreTransporterClientPingable
IsolatedCoreAudioClientWorkgroup
B
v16@?0@\"NSError\"8
com.apple.shareddspd
%@/%@
TSPDumpOptions_CollectTrials
tailspin_full_sampling_period_set
Failed to get the mach port from provided workgroup: %d
com.apple.isolatedcoreaudioclient.service
IsolatedCoreAudioClientMultiplexer.cpp
q16@?0q8
com.apple.audio.isolatedcoreaudio.asyncio_
com.apple.audio.isolatedcoreaudio.asyncio
tailspin_config_free
tailspin_config_create_with_current_state
ExclaveCapability
AudioClient.cpp
SingleUseTraceManager.mm
 
SiphonClientMap.cpp
ICAC Generated Dump
ServerSideAudioSwitchboard.cpp
v24@?0@\"IOThreadXPCSemaphoreTransporter\"8@\"IOThreadXPCMappedMemoryTransporter\"16
com.apple.private.isolated.audio.coreaudioclient.shareddsp
v12@?0i8
TSPDumpOptions_Symbolicate
tailspin_enabled_set
tailspin_kdbg_filter_subclass_set
IOThreading
v12@?0B8
v8@?0
IOThreadXPCWorkgroupTransporter
q8@?0
thread constructor failed
TSPDumpOptions_ReasonString
IsolatedCoreAudioClient
/Library/Caches/com.apple.xbs/4BC2D3CD-BEF8-4096-9422-AC5A706FDBC0/TemporaryDirectory.8poeh2/Binaries/IsolatedCoreAudioClient/install/TempContent/Objects/IsolatedCoreAudioClient.build/IsolatedCoreAudioClient.build/DerivedSources/IsolatedCor
IsolatedCoreAudioFlags.cpp
Error on remote object proxy
ClientSideAudioSwitchboard.cpp
TB_FATAL: invalid value: unexpected case value, %llx (%s:%d)\n
%25s:%-5d  Description:\t%@
%25s:%-5d  Reason:\t\t%@
%25s:%-5d CreateIsolatedAudioSiphonPortal unsupported
%25s:%-5d AudioClient::stop - The client has tried to stop IO, but IO is already being started or stopped by the client.
%25s:%-5d Client stopped consuming timestamps. Skipping timestamp callback.
%25s:%-5d ClientSideAudioSwitchboardIOThread::IOTearDownFunction - Failed to leave the workgroup!!!! - %d
%25s:%-5d IsolatedCoreAudioXPCService - checkInForIsolatedAudioSharedResources - after registering
%25s:%-5d Hello Siphon Tests
%25s:%-5d ServerSideHardware::DeRegisterCallback - Failed to destroy audio device IO proc - error: %s
%25s:%-5d AudioClient::stop - Failed to stop isolated DSP, %d
%25s:%-5d XPCConnectionToServer::acquireSharedIOThreadResourcesFromServer - after call
%25s:%-5d IsolatedCoreAudioClientMultiplexer::startSharedIO failed to start for use case %s with status %d
%25s:%-5d %s called Start IO
%25s:%-5d AudioClientBase::getClient - client:%p...
%25s:%-5d RemoteAudioHardwareServer::RemoteAudioHardwareServer::InvalidationHandler - Connection invalidated!!!
%25s:%-5d ClientSideAudioSwitchboard::ServerDeathMessage - server disappeared!
%25s:%-5d ClientSideAudioSwitchboardIOThread::TranslateKernelError - General Semaphore Error - %d. Exiting the workloop
%25s:%-5d IsolatedCoreAudioXPCService - checkInForIsolatedAudioSharedResources
%25s:%-5d ClientSideAudioSwitchboard::startIOProc Failed! Start Conditions: %s
%25s:%-5d ServerSideAudioSwitchboard::startServerIOThread IO not started for client %s
%25s:%-5d SiphonIOClient: Lapse callback threw an exception.
%25s:%-5d Client is starting IO without setting a callback.
%25s:%-5d Trace has already been written
%25s:%-5d IOThread::createPOSIXThread() : failed to set the scheduling policy
%25s:%-5d Received CreateIsolatedAudioSiphonPortal request
%25s:%-5d setAudioAvailabilityCallback called
%25s:%-5d ReverseSiphonDelegate AudioAvailabilityCallback failed.
%25s:%-5d IsolatedCoreAudioClientNSXPCListenerDelegate - invalidationHandler
%25s:%-5d ServerSideHardware::StartIOProcAtTime - Failed to start audio device - error: %s
%25s:%-5d Reverse connection invalidated
%25s:%-5d Dropping tailspin to %@
%25s:%-5d Received CreateIsolatedAudioServicePortal request
%25s:%-5d ClientSideAudioSwitchboardIOThread::spawnIOThread - Provided workgroup is invalid!!!!
%25s:%-5d IsolatedCoreAudioXPCService - checkInForIsolatedAudioSharedResources - after allocating semaphore transporter
%25s:%-5d IsolatedCoreAudioXPCService - startIsolatedAudioForUseCaseAtTime - landed in the catch!
%25s:%-5d ServerSideAudioSwitchboard::addClientUseCase stopping IO for unresponsive client %s
%25s:%-5d ClientSideAudioSwitchboardIOThread::IOSetUpFunction - timed out waiting for signal from server.
%25s:%-5d IsolatedCoreAudioXPCService - checkInForIsolatedAudioSharedResources - after adding client
%25s:%-5d %@: %@ %@\n
%25s:%-5d AudioClientBase::getClient...
%25s:%-5d ClientSideAudioSwitchboardIOThread::IOMainWorkloopFunction - heading for the egress.
%25s:%-5d IsolatedCoreAudioXPCService - after to reply in checkInForIsolatedAudioSharedResources
%25s:%-5d Process %i does not have the %@ entitlement
%25s:%-5d ServerSideHardware::StartIOProc - Failed to start audio device - error: %s
%25s:%-5d CreateIsolatedAudioServicePortal allocating portal
%25s:%-5d AudioClient::stop - Unknown exception caught.
%25s:%-5d ICAC using BlockingTimestampQueue
%25s:%-5d %s called Stop IO
%25s:%-5d Completed async tailspin drop - %@
%25s:%-5d CreateIsolatedAudioServicePortal unsupported
%25s:%-5d IsolatedCoreAudioXPCService - Stop
%25s:%-5d IsolatedCoreAudioXPCService - stopIsolatedAudioForUseCase - landed in the catch!
%25s:%-5d Hello Siphon
%25s:%-5d Waiting for Availability callbacks to complete for %s client
%25s:%-5d Attempting to apply testing config resulted in: %s
%25s:%-5d ServerSideHardware::AttachCallbacksToHALDevice - Failed to create audio device IO proc - error: %s
%25s:%-5d Error getting IsolateCoreAudioClient TightBeam endpoint - this should not happen!!! ErrorCode: %u
%25s:%-5d IsolatedCoreAudioClientMultiplexer::stopIOIfNoClientsAreRunning No server IO running but we think some clients are running IO ???!!?
%25s:%-5d HALUseCase::SetDeviceIDUsingUseCaseID mDeviceID: %u
%25s:%-5d The tailspin dylib does not exist
%25s:%-5d ServerSideHardware::AttachCallbacksToHALDevice - IOProcID succeeded
%25s:%-5d ServerSideHardware::StopIOProc - Stopped audio device
%25s:%-5d Created tailspin at: %s
%25s:%-5d Cleared tailspin directory
%25s:%-5d IOThread::createPOSIXThread() : failed to set the priority
%25s:%-5d XPCConnectionToServer::acquireSharedIOThreadResourcesFromServer - in reply call
%25s:%-5d ServerSideHardware::StopIOProc - Failed to stop audio device - error: %s
%25s:%-5d ServerSideHardware::AttachCallbacksToHALDevice - Skipping creating IO proc installation, device hasn't changed
%25s:%-5d ServerSideHardware::StartIOProc - Started audio device
%25s:%-5d Received CreateHistoricalAudioPortal request
%25s:%-5d IsolatedCoreAudioClientMultiplexer::stopIOIfNoClientsAreRunning Stop requested, not stopping IO, as some clients still running
%25s:%-5d Could not create get workgroup for deviceID: %u because of Error:%@
%25s:%-5d Stopping IO on the %s client
%25s:%-5d IsolatedCoreAudioClientMultiplexer::startIOIfNoClientsAreRunning IO failed to start with status %d
%25s:%-5d IsolatedCoreAudioXPCService - checkInForIsolatedAudioSharedResources - landed in the catch!
%25s:%-5d IsolatedCoreAudioXPCService - getWorkgroupForIsolatedAudio - landed in the catch!
%25s:%-5d SiphonIOClient::setHasStartedIO - Dispatch Queue has been flushed
%25s:%-5d Attempting to dump %s tailspin
%25s:%-5d Failed to create file descriptor for - %@
%25s:%-5d ServerSideAudioSwitchboard::GetClientForIO - No client exists for %u!
%25s:%-5d CreateIsolatedAudioSiphonPortal allocating portal
%25s:%-5d IsolatedCoreAudioClientMultiplexer::stopIOIfNoClientsAreRunning sending Stop message to server
%25s:%-5d IsolatedCoreAudioXPCSiphon - requestAudio Landed in the catch!
%25s:%-5d Stopping IO for %s client after losing connection to their process recently at pid %d
%25s:%-5d ClientSideAudioSwitchboardIOThread::TranslateKernelError - Semaphores timed out!!! Exiting the workloop
%25s:%-5d Creating default tailspin manager
%25s:%-5d ServerSideHardware::RegisterCallback - legacyHalUseCase is unknown!
%25s:%-5d IsolatedCoreAudioXPCService - checkOutForIsolatedAudioSharedResources
%25s:%-5d ReverseSiphonDelegate LapseCallback failed.
%25s:%-5d ServerSideHardware::StartIOProcAtTime - Started audio device
%25s:%-5d  Suggestion:\t%@
%25s:%-5d AudioClient::startAtTime - The client has tried to start IO, but client IO is already running.
%25s:%-5d ClientSideAudioSwitchboardIOThread::IOSetUpFunction - Failed to join the workgroup!!!! - %d
%25s:%-5d IsolatedCoreAudioXPCService - Start
%25s:%-5d IsolatedCoreAudioXPCService - StartAtTime
%25s:%-5d ClientSideAudioSwitchboard::handleErrorConditions Failed to receive ping from local client thread
%25s:%-5d AudioClient::start - Failed to start isolated DSP, %d
%25s:%-5d IsolatedCoreAudioXPCService - checkInForIsolatedAudioSharedResources - after exporting
%25s:%-5d IsolatedCoreAudioXPCService - checkInForIsolatedAudioSharedResources - after allocating memory transporter
%25s:%-5d Synchronous StopIO Complete for %s client
%25s:%-5d IsolatedCoreAudioClientMultiplexer::stopIOIfNoClientsAreRunning Stop requested, but no client IO (and server) is running IO
%25s:%-5d ClientSideAudioSwitchboardIOThread::IOSetUpFunction - unknown error occurred waiting for signal from server.
%25s:%-5d ClientSideAudioSwitchboardIOThread::IOMainWorkloopFunction - timed out waiting for signal from server.
%25s:%-5d Reverse connection interrupted
%25s:%-5d XPCConnectionToServer::acquireSharedIOThreadResourcesFromServer - before call
%25s:%-5d IsolatedCoreAudioXPCService - Normal INIT
%25s:%-5d Failed to drop async tailspin - %@
%25s:%-5d LogRetrySetDeviceIDState - Failed to set device ID for use case ID for %u tries in %f seconds
%25s:%-5d IsolatedCoreAudioClientMultiplexer::startIOIfNoClientsAreRunning IO already running
%25s:%-5d HALUseCase::SetDeviceIDUsingUseCaseID looking for: %u
%25s:%-5d Enabling lapse handling on %s client
%25s:%-5d ServerSideAudioSwitchboard::addClientUseCase client %s already exists
%25s:%-5d ServerSideHardware::DeRegisterCallback - IOProcID destruction succeeded
%25s:%-5d  Code:\t\t\t%ld
%25s:%-5d AudioClient::start - The client has tried to start IO, but client IO is already running.
%25s:%-5d setAudioLapseCallback called
%25s:%-5d IsolatedCoreAudioXPCSiphon - stopIO Landed in the catch!
%25s:%-5d AudioClientBase::createDedicatedClient...
%25s:%-5d Attempting to apply default tailspin config resulted in: %s
%25s:%-5d IOThread::createPOSIXThread() : failed to get the default scheduling parameters
%25s:%-5d IsolatedCoreAudioClientNSXPCListenerDelegate - Listener
%25s:%-5d AudioClient::start - Unknown exception caught.
%25s:%-5d AudioClient::start - There was an error trying to start IO, %d
%25s:%-5d AudioClient::stop - The client has tried to stop IO, but IO is not running.
%25s:%-5d Disabling lapse handling on %s client
%25s:%-5d ServerSideAudioSwitchboard::registerForIO client %s is already registered for IO
%25s:%-5d hardwareSupportsExclaves: %d
%25s:%-5d ClientSideAudioSwitchboardIOThread::IOSetUpFunction - Failed to set the RT thread priority!!!! - %d
%25s:%-5d IsolatedCoreAudioXPCSiphon - setAudioAvailabilityCallback Landed in the catch!
%25s:%-5d IOThread::createPOSIXThread() : the attributes could not be created
%25s:%-5d IsolatedCoreAudioClientNSXPCListenerDelegate - interruptionHandler
%25s:%-5d AudioClient::startAtTime - The client has tried to start IO, but IO is already being started or stopped by the client.
%25s:%-5d AudioClient::startAtTime - There was an error trying to start IO at the given time.
%25s:%-5d IsolatedCoreAudioXPCService - getWorkgroupForIsolatedAudio
%25s:%-5d ClientSideAudioSwitchboard::defaultIOThreadExitHandler - Local IO Thread has exited.
%25s:%-5d Failed to create file descriptor - %@
%25s:%-5d ServerSideAudioSwitchboard::addClient - Client %u already present in map!
%25s:%-5d IOThread::createPOSIXThread() : failed to create the thread
%25s:%-5d AudioClient::start - The client has tried to start IO, but IO is already being started or stopped by the client.
%25s:%-5d XPCConnectionToServer::releaseSharedIOThreadResourcesFromServer - before call
%25s:%-5d Failed to drop tailspin - %@
%25s:%-5d ServerSideAudioSwitchboard::stopServerIOThread IO not stopped for client %s
%25s:%-5d XPCConnectionToServer::makeXPCConnectionToServer Received CreateIsolatedAudioServicePortal request
%25s:%-5d Attempt to connect to IsolatedAudio sever via XPC failed.
%25s:%-5d AudioClient::startAtTime - Unknown exception caught.
%25s:%-5d IsolatedCoreAudioClientMultiplexer:: IO has lapsed with status %d
%25s:%-5d ClientSideAudioSwitchboardIOThread::IOTearDownFunction - Failed to set the RT thread priority!!!! - %d
%25s:%-5d IsolatedCoreAudioXPCService - checkOutForIsolatedAudioSharedResources - landed in the catch!
%25s:%-5d IsolatedCoreAudioXPCSiphon - startIO Landed in the catch!
%25s:%-5d Starting IO on the %s client
%25s:%-5d LogRetrySetDeviceIDState - Successfully set device ID after %u tries in %f seconds
%25s:%-5d XPCConnectionToServer::releaseSharedIOThreadResourcesFromServer - after call
%25s:%-5d IsolatedCoreAudioXPCService - startIsolatedAudioForUseCase - landed in the catch!
%25s:%-5d HALUseCase::SetDeviceIDUsingUseCaseID could not get device ID - looking for %u and received error: %s 
%25s:%-5d AudioClientBase::createUnitTestClient...
%25s:%-5d translateFerryToSinkStatus encountered an error! Result: %d
%25s:%-5d IsolatedCoreAudioClientMultiplexer:: IO lapsed during rendezvous.
```
