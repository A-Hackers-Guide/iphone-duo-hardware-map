# `/usr/lib/updaters/libMantaMCUUpdater.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 11,925,264 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 43 (Size: 6888)
Flags         = NoUndefs, DyldLink, TwoLevel, WeakDefines, BindsToWeak, NoReexportedDylibs, HasTLVDescriptors, AppExtensionSafe, NlistOutofsyncWithDyldinfo
```

## Linked libraries (26)

- `/usr/lib/updaters/libMantaMCUUpdater.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/System/Library/PrivateFrameworks/RemoteXPC.framework/RemoteXPC (compatibility version 1.0.0, current version 3298.52.1, weak)`
- `/System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery (compatibility version 1.0.0, current version 245.40.9, weak)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration (compatibility version 1.0.0, current version 1453.40.1)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.12)`
- `/usr/lib/swift/libswiftCore.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftCoreFoundation.dylib (compatibility version 1.0.0, current version 120.100.0)`
- `/usr/lib/swift/libswiftDarwin.dylib (compatibility version 1.0.0, current version 428.40.1)`
- `/usr/lib/swift/libswiftDispatch.dylib (compatibility version 1.0.0, current version 1605.40.4)`
- `/usr/lib/swift/libswiftOSLog.dylib (compatibility version 1.0.0, current version 10.0.0, weak)`
- `/usr/lib/swift/libswiftObjectiveC.dylib (compatibility version 1.0.0, current version 973.1.0)`
- `/usr/lib/swift/libswiftXPC.dylib (compatibility version 1.0.0, current version 167.0.2)`
- `/usr/lib/swift/libswift_Builtin_float.dylib (compatibility version 0.0.0, current version 0.0.0, weak)`
- `/usr/lib/swift/libswift_Concurrency.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswift_DarwinFoundation1.dylib (compatibility version 1.0.0, current version 428.40.1)`
- `/usr/lib/swift/libswift_DarwinFoundation2.dylib (compatibility version 1.0.0, current version 428.40.1)`
- `/usr/lib/swift/libswift_DarwinFoundation3.dylib (compatibility version 1.0.0, current version 428.40.1)`
- `/usr/lib/swift/libswift_StringProcessing.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftos.dylib (compatibility version 1.0.0, current version 1090.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (160 classes, 5 protocols)

Classes: `MRUHardwareInfo`, `MRULogHelper`, `MRUPersonalizationInfo`, `MRUPersonalizedFirmware`, `_TtC10Subprocess12CStringArray`, `_TtC11IOKitExtras18IOKitManagedHandle`, `_TtC11IOKitExtras26IOServiceDiscoverySequence`, `_TtC11IOKitExtras40IOServiceDiscoverySequenceImplementation`, `_TtC11NIOEmbedded15EmbeddedChannel`, `_TtC11NIOEmbedded17EmbeddedEventLoop`, `_TtC11NIOEmbedded19EmbeddedChannelCore`, `_TtC11NIOEmbedded22NIOAsyncTestingChannel`, `_TtC11NIOEmbedded24NIOAsyncTestingEventLoop`, `_TtC11NIOEmbeddedP33_B74500E45D63218F027FB4553B6BF95020PromiseCreationStore`, `_TtC11RT13Updater10B2PDecoder`, `_TtC11RT13Updater10B2PEncoder`, `_TtC11RT13Updater11B2PChecksum`, `_TtC11RT13Updater13RT13DFUClient`, `_TtC11RT13Updater14RestoreDecoder`, `_TtC11RT13Updater14RestoreEncoder`, `_TtC11RT13Updater16B2PMessageLogger`, `_TtC11RT13Updater17RT13RestoreClient`, `_TtC11RT13Updater20RestoreMessageLogger`, `_TtC11RT13Updater23B2PClientChannelHandler`, `_TtC11RT13Updater27RestoreClientChannelHandler`, `_TtC13MantaFirmware34MantaLocalDataBaseFirmwareProvider`, `_TtC13TracingExtras14OSSignpostSpan`, `_TtC13TracingExtras16OSSignpostTracer`, `_TtC14KalElUIService15UIServiceClient`, `_TtC14KalElUIService15UIServiceServer`, `_TtC14KalElUIService22UIServiceMessageLogger`, `_TtC14KalElUIService26UIServiceRawMessageDecoder`, `_TtC14KalElUIService26UIServiceRawMessageEncoder`, `_TtC14KalElUIService29UIServiceClientChannelHandler`, `_TtC14KalElUIService29UIServiceServerChannelHandler`, `_TtC14KalElUtilities5Queue`, `_TtC14MantaUtilities5Queue`, `_TtC14MantaUtilities9Semaphore`, `_TtC15Instrumentation13ReadWriteLock`, `_TtC15MantaMCUUpdater19MantaMCUUpdaterShim`, `_TtC16KalElBootService17BootServiceClient`, `_TtC16KalElBootService18BootServiceChannel`, `_TtC16KalElBootService19MantaAsyncUDPRouter`, `_TtC16KalElBootService23BootServiceRemoteDevice`, `_TtC16KalElBootService33BootServiceRemoteDeviceController`, `_TtC16KalElBootService9Semaphore`, `_TtC17KalElFlashService18FlashServiceClient`, `_TtC17KalElFlashService25FlashServiceMessageLogger`, `_TtC17KalElFlashService26FlashServiceMessageDecoder`, `_TtC17KalElFlashService26FlashServiceMessageEncoder`, `_TtC17KalElFlashService38FlashServiceClientUpdateChannelHandler`, `_TtC17MantaAppleConnect19AppleConnectManager`, `_TtC17MantaXPCAPIModule14MantaXPCClient`, `_TtC17MantaXPCAPIModule14MantaXPCServer`, `_TtC17MantaXPCAPIModule22MantaXPCInternalClient`, `_TtC17MantaXPCAPIModule22MantaXPCInternalServer`, `_TtC17MantaXPCAPIModule26MantaRemoteXPCPublicClient`, `_TtC17MantaXPCAPIModule26MantaRemoteXPCPublicServer`, `_TtC17MantaXPCAPIModule5Queue`, `_TtC18KalElSignalService19SignalServiceClient`, `_TtC18KalElSignalService26SignalServiceMessageLogger`, `_TtC18KalElSignalService27SignalServiceMessageDecoder`, `_TtC18KalElSignalService27SignalServiceMessageEncoder`, `_TtC18KalElSignalService33SignalServiceClientChannelHandler`, `_TtC19MantaAsyncXPCModule16XPCObjectDecoder`, `_TtC19MantaAsyncXPCModule16XPCObjectEncoder`, `_TtC19MantaAsyncXPCModule17_XPCObjectDecoder`, `_TtC19MantaAsyncXPCModule17_XPCObjectEncoder`, `_TtC19MantaAsyncXPCModule21MantaAsyncXPCListener`, `_TtC19MantaAsyncXPCModule23MantaAsyncXPCConnection`, `_TtC19MantaAsyncXPCModule32AsyncRemoteDeviceBrowserSequence`, `_TtC19MantaAsyncXPCModule40AsyncRemoteDeviceConnectionEventSequence`, `_TtC19MantaMCUUpdaterCore12OTAPreflight`, `_TtC19MantaMCUUpdaterCore16UpdateController`, `_TtC19MantaMCUUpdaterCore18GenericErrorSource`, `_TtC19MantaMCUUpdaterCore22BootedOSUpdateStrategy`, `_TtC19MantaMCUUpdaterCore23RestoreOSUpdateStrategy`, `_TtC20MantaKalElController15KalElController`, `_TtC20MantaKalElController32KalElControllerMultiplexDelegate`, `_TtC21AsyncAlgorithmsExtras18AsyncInterruptCore`, `_TtC21AsyncAlgorithmsExtras21AsyncInterruptTrigger`, `_TtC21MantaTriageController12MarvinTriage`, `_TtC21MantaTriageController13TriageHelpers`, `_TtC21MantaTriageController15AstrisRawTriage`, `_TtC21MantaTriageController16TriageController`, `_TtC21MantaTriageController18AstrisNativeTriage`, `_TtC21NIOConcurrencyHelpers4Lock`, `_TtC22MantaRetimerController14RetimerWatcher`, `_TtC22MantaRetimerController17RetimerController`, `_TtC22MantaRetimerController7Retimer`, `_TtC23KalElFactoryDataService24FactoryDataServiceClient`, `_TtC23KalElFactoryDataService31FactoryDataServiceMessageLogger`, `_TtC23KalElFactoryDataService32FactoryDataServiceMessageDecoder`, `_TtC23KalElFactoryDataService32FactoryDataServiceMessageEncoder`, `_TtC23KalElFactoryDataService38FactoryDataServiceClientChannelHandler`, `_TtC23MantaMCUTraceController15MCUTraceHandler`, `_TtC23MantaMCUTraceController18MCUTraceController`, `_TtC23MantaMCUTraceController9MCUTracer`, `_TtC7Logging13ReadWriteLock`, `_TtC7Logging4Lock`, `_TtC7NIOCore11DeadChannel`, `_TtC7NIOCore12RepeatedTask`, `_TtC7NIOCore13NIOFileHandle`, `_TtC7NIOCore15ChannelPipeline`, `_TtC7NIOCore16IdleStateHandler`, `_TtC7NIOCore18HeadChannelHandler`, `_TtC7NIOCore18TailChannelHandler`, `_TtC7NIOCore19BackPressureHandler`, `_TtC7NIOCore19NIONetworkInterface`, `_TtC7NIOCore20AcceptBackoffHandler`, `_TtC7NIOCore21ChannelHandlerContext`, `_TtC7NIOCore22NIOCloseOnErrorHandler`, `_TtC7NIOCoreP33_5D1691F81BFB9463F74AA8273C0A4D2D15DeadChannelCore`, `_TtC8MantaEDM17EmbeddedDeviceMap`, `_TtC8NIOPosix10BaseSocket`, `_TtC8NIOPosix12ServerSocket`, `_TtC8NIOPosix13NIOThreadPool`, `_TtC8NIOPosix15ClientBootstrap`, `_TtC8NIOPosix15ServerBootstrap`, `_TtC8NIOPosix16NIOPipeBootstrap`, `_TtC8NIOPosix17DatagramBootstrap`, `_TtC8NIOPosix19GetaddrinfoResolver`, `_TtC8NIOPosix19SelectableEventLoop`, `_TtC8NIOPosix22HappyEyeballsConnector`, `_TtC8NIOPosix26PendingStreamWritesManager`, `_TtC8NIOPosix27MultiThreadedEventLoopGroup`, `_TtC8NIOPosix28PendingDatagramWritesManager`, `_TtC8NIOPosix6Socket`, `_TtC8NIOPosix8PipePair`, `_TtC8NIOPosix9NIOThread`, `_TtC8TCPProxy11GlueHandler`, `_TtC8TCPProxy15TCPProxyHandler`, `_TtC8TCPProxy19CloseOnErrorHandler`, `_TtC8TCPProxy8TCPProxy`, `_TtC9NIOExtras17NIOPCAPRingBuffer`, `_TtC9NIOExtras19NIOWritePCAPHandler`, `_TtC9NIOExtras20LengthFieldPrepender`, `_TtC9NIOExtras21LineBasedFrameDecoder`, `_TtC9NIOExtras21ServerQuiescingHelper`, `_TtC9NIOExtras23FixedLengthFrameDecoder`, `_TtC9NIOExtras25DebugInboundEventsHandler`, `_TtC9NIOExtras26DebugOutboundEventsHandler`, `_TtC9NIOExtras28LengthFieldBasedFrameDecoder`, `_TtC9NIOExtrasP33_15131B0A1C2B96335CB419BAF83D55DE16ChannelCollector`, `_TtC9NIOExtrasP33_15131B0A1C2B96335CB419BAF83D55DE30CollectAcceptedChannelsHandler`, `_TtC9SerialLog11SerialProxy`, `_TtC9SerialLog16LineToLogHandler`, `_TtC9SerialLog19SerialConsoleClient`, `_TtC9SerialLog19SerialConsoleServer`, `_TtC9SerialLog22SerialLogCaptureClient`, `_TtCC8NIOPosix15ServerBootstrapP33_F13D6D61D4A528D08BD67995505C248713AcceptHandler`, `_TtCC9NIOExtras19NIOWritePCAPHandler20SynchronizedFileSink`, `_TtCE25SystemConfigurationExtrasaSo16SCPreferencesRef4Info`, `_TtCE25SystemConfigurationExtrasaSo17SCDynamicStoreRef4Info`, `_TtCO7Logging13LoggingSystemP33_C9FF2A9F0C61C813477A18DFECB0159A10FactoryBox`, `_TtCO9NIOExtras17NIOJSONRPCFraming31ContentLengthHeaderFrameEncoder`, `_TtCV21NIOConcurrencyHelpers7NIOLock8_Storage`, `_TtCV7NIOCore10ByteBuffer8_Storage`, `_TtCV7NIOCore16NIONetworkDeviceP33_332F4CD194A63D42AC43F87173201E7D7Backing`, `_TtCV7Tracing10NoOpTracer8NoOpSpan`

Protocols: `NSCoding`, `NSObject`, `OS_dispatch_source`, `OS_dispatch_source_signal`, `OS_xpc_object`

## Strings (9,796)

First 2,500 of 9,796.
```
MRUHardwareInfo
_TtC8NIOPosix22HappyEyeballsConnector
_TtC19MantaAsyncXPCModule16XPCObjectEncoder
_TtC7NIOCore16IdleStateHandler
_TtC7NIOCore18TailChannelHandler
_TtC8NIOPosix9NIOThread
_TtC17MantaXPCAPIModule22MantaXPCInternalServer
_TtC8TCPProxy11GlueHandler
_TtCE25SystemConfigurationExtrasaSo16SCPreferencesRef4Info
_TtC14MantaUtilities5Queue
MRUPersonalizationInfo
_TtC18KalElSignalService27SignalServiceMessageEncoder
_TtC13TracingExtras14OSSignpostSpan
_TtC13TracingExtras16OSSignpostTracer
_TtC22MantaRetimerController17RetimerController
_TtC21AsyncAlgorithmsExtras21AsyncInterruptTrigger
_TtC7NIOCore11DeadChannel
_TtC8NIOPosix11PipeChannel
_TtC17KalElFlashService38FlashServiceClientUpdateChannelHandler
_TtC11RT13Updater16B2PMessageLogger
_TtC11NIOEmbedded22NIOAsyncTestingChannel
_TtC11NIOEmbeddedP33_B74500E45D63218F027FB4553B6BF95020PromiseCreationStore
_TtC23KalElFactoryDataService32FactoryDataServiceMessageEncoder
_TtC11RT13Updater17RT13RestoreClient
_TtC11NIOEmbedded17EmbeddedEventLoop
_TtC8NIOPosix28PendingDatagramWritesManager
_TtC17KalElFlashService26FlashServiceMessageDecoder
_TtC14KalElUIService29UIServiceServerChannelHandler
_TtC14KalElUIService15UIServiceClient
_TtC21MantaTriageController18AstrisNativeTriage
_TtC11RT13Updater11B2PChecksum
_TtC11NIOEmbedded24NIOAsyncTestingEventLoop
_TtC18KalElSignalService33SignalServiceClientChannelHandler
_TtC14KalElUIService29UIServiceClientChannelHandler
_TtCV7NIOCore16NIONetworkDeviceP33_332F4CD194A63D42AC43F87173201E7D7Backing
_TtC17KalElFlashService25FlashServiceMessageLogger
_TtC14KalElUIService15UIServiceServer
_TtC22MantaRetimerController14RetimerWatcher
_TtCV7NIOCore10ByteBuffer8_Storage
_TtC23KalElFactoryDataService31FactoryDataServiceMessageLogger
_TtC8TCPProxy15TCPProxyHandler
_TtC15MantaMCUUpdater19MantaMCUUpdaterShim
_TtC19MantaMCUUpdaterCore22BootedOSUpdateStrategy
_TtC7NIOCore22NIOCloseOnErrorHandler
_TtCV21NIOConcurrencyHelpers7NIOLock8_Storage
_TtC23KalElFactoryDataService38FactoryDataServiceClientChannelHandler
_TtCV7Tracing10NoOpTracer8NoOpSpan
_TtC11RT13Updater13RT13DFUClient
_TtC7NIOCore13NIOFileHandle
_TtC11IOKitExtras18IOKitManagedHandle
_TtC8NIOPosix26PendingStreamWritesManager
_TtC16KalElBootService18BootServiceChannel
_TtC23MantaMCUTraceController18MCUTraceController
_TtC11RT13Updater20RestoreMessageLogger
_TtC19MantaMCUUpdaterCore12OTAPreflight
NSCoding
_TtC8NIOPosix17DatagramBootstrap
_TtC8NIOPosix19SelectableEventLoop
_TtC16KalElBootService23BootServiceRemoteDevice
_TtC14KalElUIService22UIServiceMessageLogger
_TtC19MantaAsyncXPCModule17_XPCObjectEncoder
_TtC7Logging4Lock
_TtC8MantaEDM17EmbeddedDeviceMap
_TtC23KalElFactoryDataService32FactoryDataServiceMessageDecoder
_TtC13MantaFirmware34MantaLocalDataBaseFirmwareProvider
_TtC19MantaAsyncXPCModule17_XPCObjectDecoder
_TtC15Instrumentation13ReadWriteLock
_TtC23MantaMCUTraceController9MCUTracer
_TtC21MantaTriageController16TriageController
_TtCO7Logging13LoggingSystemP33_C9FF2A9F0C61C813477A18DFECB0159A10FactoryBox
_TtC8NIOPosix15ClientBootstrap
_TtC17KalElFlashService18FlashServiceClient
_TtC14KalElUIService26UIServiceRawMessageDecoder
_TtC17MantaXPCAPIModule22MantaXPCInternalClient
_TtC17MantaXPCAPIModule5Queue
_TtC9NIOExtrasP33_15131B0A1C2B96335CB419BAF83D55DE16ChannelCollector
_TtC8TCPProxy19CloseOnErrorHandler
_TtC19MantaMCUUpdaterCore23RestoreOSUpdateStrategy
_TtC7NIOCore19BackPressureHandler
_TtC7NIOCore21ChannelHandlerContext
_TtC19MantaAsyncXPCModule21MantaAsyncXPCListener
_TtC17MantaXPCAPIModule26MantaRemoteXPCPublicClient
_TtC21MantaTriageController15AstrisRawTriage
_TtC21MantaTriageController12MarvinTriage
_TtC11RT13Updater10B2PEncoder
_TtC8NIOPosix8PipePair
OS_dispatch_source
_TtC9SerialLog19SerialConsoleClient
_TtC11RT13Updater27RestoreClientChannelHandler
_TtC7Logging13ReadWriteLock
_TtCE25SystemConfigurationExtrasaSo17SCDynamicStoreRef4Info
_TtC14MantaUtilities9Semaphore
MRULogHelper
_TtC7NIOCore12RepeatedTask
_TtC8NIOPosix15DatagramChannel
_TtC9NIOExtras19NIOWritePCAPHandler
_TtC10Subprocess12CStringArray
_TtC7NIOCore18HeadChannelHandler
_TtC11NIOEmbedded15EmbeddedChannel
_TtC8NIOPosix13NIOThreadPool
_TtC17MantaXPCAPIModule26MantaRemoteXPCPublicServer
_TtC17MantaXPCAPIModule14MantaXPCServer
_TtCC9NIOExtras19NIOWritePCAPHandler20SynchronizedFileSink
_TtC8NIOPosix10BaseSocket
_TtC17KalElFlashService26FlashServiceMessageEncoder
NSObject
_TtC9NIOExtras21LineBasedFrameDecoder
_TtC20MantaKalElController32KalElControllerMultiplexDelegate
_TtC14KalElUtilities5Queue
_TtC16KalElBootService17BootServiceClient
_TtC14KalElUIService26UIServiceRawMessageEncoder
_TtC19MantaAsyncXPCModule40AsyncRemoteDeviceConnectionEventSequence
_TtC9NIOExtras28LengthFieldBasedFrameDecoder
_TtC11RT13Updater14RestoreEncoder
MRUPersonalizedFirmware
_TtC17MantaAppleConnect19AppleConnectManager
_TtC8NIOPosix13SocketChannel
_TtC16KalElBootService19MantaAsyncUDPRouter
_TtC16KalElBootService33BootServiceRemoteDeviceController
_TtC9NIOExtras17NIOPCAPRingBuffer
_TtC9SerialLog19SerialConsoleServer
OS_dispatch_source_signal
OS_xpc_object
_TtC19MantaAsyncXPCModule32AsyncRemoteDeviceBrowserSequence
_TtC9SerialLog22SerialLogCaptureClient
_TtC22MantaRetimerController7Retimer
_TtC11RT13Updater14RestoreDecoder
_TtC11NIOEmbedded19EmbeddedChannelCore
_TtC23KalElFactoryDataService24FactoryDataServiceClient
_TtC9NIOExtras26DebugOutboundEventsHandler
_TtC8TCPProxy8TCPProxy
_TtC8NIOPosix16NIOPipeBootstrap
_TtC19MantaAsyncXPCModule16XPCObjectDecoder
_TtC9SerialLog16LineToLogHandler
_TtC16KalElBootService9Semaphore
_TtC18KalElSignalService19SignalServiceClient
_TtC9NIOExtras23FixedLengthFrameDecoder
_TtC21MantaTriageController13TriageHelpers
_TtC11RT13Updater23B2PClientChannelHandler
_TtC7NIOCore20AcceptBackoffHandler
_TtCC8NIOPosix15ServerBootstrapP33_F13D6D61D4A528D08BD67995505C248713AcceptHandler
_TtC8NIOPosix12ServerSocket
_TtC18KalElSignalService27SignalServiceMessageDecoder
_TtC19MantaAsyncXPCModule23MantaAsyncXPCConnection
_TtC9NIOExtras20LengthFieldPrepender
_TtC9NIOExtrasP33_15131B0A1C2B96335CB419BAF83D55DE30CollectAcceptedChannelsHandler
_TtC7NIOCore19NIONetworkInterface
_TtCO9NIOExtras17NIOJSONRPCFraming31ContentLengthHeaderFrameEncoder
_TtC11RT13Updater10B2PDecoder
_TtC17MantaXPCAPIModule14MantaXPCClient
_TtC7NIOCore15ChannelPipeline
_TtC7NIOCoreP33_5D1691F81BFB9463F74AA8273C0A4D2D15DeadChannelCore
_TtC11IOKitExtras26IOServiceDiscoverySequence
_TtC8NIOPosix19ServerSocketChannel
_TtC21AsyncAlgorithmsExtras18AsyncInterruptCore
_TtC9NIOExtras25DebugInboundEventsHandler
_TtC9NIOExtras21ServerQuiescingHelper
_TtC19MantaMCUUpdaterCore16UpdateController
_TtC11IOKitExtras40IOServiceDiscoverySequenceImplementation
_TtC8NIOPosix15ServerBootstrap
_TtC9SerialLog11SerialProxy
_TtC21NIOConcurrencyHelpers4Lock
_TtC8NIOPosix19GetaddrinfoResolver
_TtC8NIOPosix27MultiThreadedEventLoopGroup
_TtC18KalElSignalService26SignalServiceMessageLogger
_TtC19MantaMCUUpdaterCore18GenericErrorSource
_TtC8NIOPosix6Socket
_TtC20MantaKalElController15KalElController
_TtC23MantaMCUTraceController15MCUTraceHandler
delay
eventWriter
state
internalManagementInterfaceBSDName
mode
promiseCreationStore
removalState
triageController
reading
dispatchQueue
setStandardOutput:
unsignedLongLongValue
updateFirstStageBootloader
userTriggeredRemovalStarted
completed
encodeWithCoder:
nonPostedMessageHandlers
onConnectionTerminationImminent
_boardID
appendString:
bootConfiguration
eventLoopGroup
rangeAtIndex:
logTag
next
removeItemAtPath:error:
computeSerial
connectionTask
TQ,R,V_ecid
T#,R
_addressCache
topLevelStorage
device
resolutionPromise
isActive
isProxy
_streamContinuation
copyItemAtURL:toURL:error:
unsignedCharValue
_securityMode
currentPacket
getRT13Count
openChannels
remoteAddress
prev
writeSpinCount
TI,R,V_securityEpoch
loggers
isInvalidated
logger
topLevelObject
T@\"NSData\",R,V_nonce
_componentNameSuffix
aiSocktype
host
nextReadDeadlineNS
optional
scheduledAllTask
ticketName
firstStageBootloaderUpdate
setArguments:
TI,R,V_boardID
connectionQueue
boolValue
firmwareByType
platform
underlyingKey
_isOpen
T@\"NSString\",R
_channelInitializer
bmcEventDelegate
complete
createDirectoryAtURL:withIntermediateDirectories:attributes:error:
fileHandleWithNullDevice
initWithPayload:manifest:
TI,R,V_securityDomain
charValue
isMemberOfClass:
mcuMultiplexedDelegate
removeHandlerInvoked
unsignedIntValue
TQ,R
inFlushNow
initWithPattern:options:error:
launchAndReturnError:
maximumBufferSize
mcuTypeName
readTimeout
serverChannel
__swift_objectForKeyedSubscript:
_selector
alwaysUpdate
capability
embeddedEventLoop
securityDomainPropertyName
createWithOptions:logSinkFunction:context:outError:
initWithCString:encoding:
nextObject
performSelector:
receivePacketInfo
baggage
_callbacks
bytes
frameLength
head
pcapCurrentBytes
retimerParentMCU
task
_logContext
allocator
closePromise
computeExclavesSerialServer
$defaultActor
currentUpdater
pendingOutboundBuffer
udpChannel
eventLoop
initWithHardwareInfo:componentName:objectName:nonce:
lastScanOffset
location
outputShutdown
stream
aiProtocol
cond
connectTimeout
ecid
helper
ioNotificationQueue
outboundHandler
callback
chipID
incomingDataHandle
sequenceNumber
channel
context
clientDelegate
_scheduledTasks
chipRev
watcher
initWithOptions:error:
socketDescription
timerGroup
firmwareVariant
stringFromDate:
astrisProxy
securityDomain
fileHandleForWriting
ioNotificationPort
stringWithFormat:
name
pendingConnect
setLaunchPath:
setObject:forKey:
lastReadTime
contentsOfDirectoryAtPath:error:
isKindOfClass:
parent
transitionQueue
computeNodeEventDelegate
kalelTriageStreamWriter
promiseBuffer
selectorFD
stateMachine
superclass
kalelTriageStream
productionModePropertyName
externalManagementInterfaceBSDName
initWithCoder:
iovecs
queue
dealloc
allowRemoteHalfClosure
connectTimeoutScheduled
noncePropertyName
TB,R,V_productionStatus
eventStream
protocolHandlers
registrationID
value
_task
fileDescriptor
lifecycleManager
mutex
shortValue
triagePolicies
unsignedIntegerValue
backoffProvider
chipIDPropertyName
loop
_isWritable
continuation
fileSink
getCount
hardwareInfo
inboundHandler
writeTimeout
embedded
id
securityModePropertyName
socketAddressToKalEl
tcpConnection
workQueue
controller
integerValue
manifest
socketHandle
timeoutTask
_pendingTaskPop
_tagNumber
productionStatus
resolver
taskNumber
archivedDataWithRootObject:requiringSecureCoding:error:
cumulationBuffer
remoteDevices
underlyingConnectionType
unicastChannelReaders
allowStaleFirmware
fullyShutdownPromise
_addresses
channelcore
enumeratorAtPath:
postedMessageHandlers
promiseCreationStoreLock
responseTimer
payload
cancellationPromise
errorHandler
standardUserDefaults
T@\"NSString\",R,C
_storage
scheduledTasks
shutdownLock
seenEOF
impl
logInternal:arguments:
connectionDelay
release
address
allDevicesLocked
description
fileHandle
steps
_localAddress
_iovecs
autoRead
getMCUCount
index
selectableEventLoop
UTF8String
performSelector:withObject:withObject:
probe
registrations
pointToPointDestinationAddress
idx
deviceAddress
threads
bindTarget
boardIDPropertyName
inputShutdown
isRecording
pendingWrites
_serverChannelOptions
errorSource
loggerTask
objectName
scheduledRead
tasksCopy
autoIncrementingAtomicId
personalizationRequestQueue
retain
retimersHWInfo
securityMode
operation
_manifest
_tasksLock
autoIncrementingAtomicSeqno
decodeObjectForKey:
initWithFormat:arguments:
scheduledWriterTask
operationSemapthore
outboundBuffer
_channel
groupedRetimers
bundleIdentifier
descriptor
objectForKey:
systemEventDelegate
timeout
_channelOptions
_objectName
inputHandle
interface
retimerEvent
capacity
inboundBuffer
performSelector:withObject:
thread
unsignedLongValue
closeAndReturnError:
ecidPropertyName
isEqual:
mcuSerial
rt13
settings
v6Future
writable
scheduled
_chipID
_logFunction
allTimeout
connection
dnsResolutions
eventLoops
eventQueue
lastWriteCompleteTime
pauseTrigger
tracers
computeProxy
readInboundBytes
unsignedShortValue
waterMark
_buffer
_isActive
isWritable
writesGroup
maximumFragments
.cxx_destruct
activePersonalizedBundle
autoSolicitStatusTask
fileHandleForReading
intValue
_offEventLoopLock
log
_value
shim
key
group
lengthBuffer
remoteListener
terminationStatus
outgoingDataHandle
processName
serviceName
socket
_securityEpoch
_childChannelOptions
codingPath
listener
connections
maxPayloadSize
sessionID
setStandardError:
_productionStatus
_nonce
encodeObject:forKey:
forceFirmwareUpdate
reportExplicitCongestionNotifications
T@\"NSString\",?,R,C
astrisPath
astrisctlPath
channelBuilderCallback
conformsToProtocol:
debugDescription
fileExistsAtPath:
_propertyNameSuffix
_securityDomain
initWithHardwareInfo:componentName:objectName:nonce:tagNumber:
_lock
_underlying
carrierMCUs
stringWithString:
asyncErrorSource
controlMessageStorage
hash
storageRefs
inputFD
_componentName
_pipeline
marvinPath
_now
identity
longLongValue
transitionTimer
_externalStateLock
cont
respondsToSelector:
retimerController
numberWithBool:
storage
netmask
basepath
pendingRead
_payload
myGroupID
tcpProxy
partner
class
log:
runState
tail
update
userInfo
TI,R,V_chipID
cArray
events
initWithChipID:chipRev:boardID:securityEpoch:productionStatus:securityMode:securityDomain:ecid:
onConnectionInvalidated
v4Future
browser
channelInitializer
lengthFieldLength
multicastChannel
bufferAllocator
mcu
closeState
frontPanelEventDelegate
initWithFileDescriptor:
isOpen
port
source
cleanupOnClose
isActiveAtomic
msgs
desiredName
initWithDomain:code:userInfo:
numberOfThreads
_succeededVoidFuture
initWithBytes:length:
ioTerminatedNotification
ipAddressTags
readPending
_throwingSource
_bufferAllocatorCache
handle
multicastSupported
nonce
T@\"NSData\",R,V_payload
URLsForDirectory:inDomains:
bootServiceClient
init
strategy
_channelCore
tag
lock
objectForKeyedSubscript:
selfAsCanDequeueWrites
_ecid
watcherEventStream
computeSerialServer
recvAllocator
retainCount
TB,R,V_securityMode
asDictionary
originalTermios
T@\"MRUHardwareInfo\",R,V_hardwareInfo
auth
scheduledTaskCounter
vectorReadManager
_hardwareInfo
computeSMCSerialServer
pendingConnections
scheduledReaderTask
resolutionDelay
$__lazy_storage_$_channelcore
mainBundle
multicastChannelReader
xpcConnection
_msgs
fileHandleWithStandardOutput
scratchBuffer
canBeShutdownIndividually
containsValueForKey:
firmware
initWithOptions:logFunction:logContext:
mcuProxy
nioChannel
rwlock
secureBootVal
__swift_setObject:forKeyedSubscript:
boardID
interestedEvent
retimers
writtenOutboundBytes
zone
_parentGroup
autorelease
mutableCopy
pendingRequest
_stateMachine
enableSerialLogs
externalSelectorFDLock
outputURL
wrappedValue
xpcEndpoint
eventsCapacity
queuedWrites
securityEpoch
sendTask
setDateFormat:
isRunningOnHost
_verbose
_yieldIDGenerator
computeNodeEventDelegates
externalState
numberWithUnsignedLongLong:
TI,R,V_chipRev
_chipRev
childChannelInit
childChannel
dictionaryWithDictionary:
initialized
inputStream
mcuTraceController
outputFD
resolutionTask
semaphore
_promiseCreationStore
bootstrap
broadcastAddress
inputStreamWriter
pipeline
stateLock
dictionaryWithObjects:forKeys:count:
firmwareProvider
pauseWaiter
pythonpath
verboseLog:
targets
internalState
mcus
pcapFragments
identityToKalEl
destroyed
attributes
channelCollectorPromise
delegate
firstMatchInString:options:range:
interfaceIndex
setTerminationHandler:
signpostID
signposter
JSONObjectWithData:options:error:
decoder
tryLock
defaultManager
maximumBytes
serverChannelInit
T@\"NSData\",R,V_manifest
_storageRefs
appendFormat:
cStringUsingEncoding:
checksum
childChannelOptions
childGroup
error
lengthFieldEndianness
localAddress
onConnectionInterrupted
publishedWritability
retimerEventWriter
self
T@\"NSDictionary\",R
isDoneWithUpdater:outError:
maxMessagesPerRead
mcuController
addresses
currentCommand
eventStreamWriter
ioMatchedNotification
lifecycleState
multicastChannelFilter
numberWithUnsignedInt:
backlog
waiters
encoder
_delegate
localListener
bootServiceDevice
fileHandleWithStandardInput
readState
remoteDevice
mcuSerialServer
_remoteAddress
delegates
execCommandWithUpdater:command:input:output:outError:
testingEventLoop
buffer
channelCollector
channelWritabilityFlag
errorWithDomain:code:userInfo:
myThread
pipePair
B56@0:8@16@24r^{__CFDictionary=}32r^^{__CFDictionary}40^^{__CFError}48
@24@0:8@16
I
B24@0:8@\"Protocol\"16
v24@0:8@16
v24@0:8@\"NSCoder\"16
@24@0:8@\"NSCoder\"16
@52@0:8I16I20I24I28B32B36I40Q44
v16@?0@\"<OS_xpc_object>\"8
v12@?0i8
Q
^v
B24@0:8#16
@16@0:8
@24@0:8:16
B24@0:8@16
B16@0:8
@\"NSNumber\"
@\"MRUHardwareInfo\"
@\"NSData\"
@\"NSString\"16@0:8
@32@0:8:16@24
@40@0:8:16@24@32
B24@0:8:16
@48@0:8r^{__CFDictionary=}16^?24^v32^^{__CFError}40
@40@0:8@16^?24^v32
^?
v16@0:8
v20@?0@\"OS_remote_device\"8B16
^{_NSZone=}16@0:8
B24@?0r*8@\"<OS_xpc_object>\"16
@32@0:8@16^@24
B
v32@0:8@16*24
v16@?0@\"OS_remote_device\"8
B32@0:8@16^^{__CFError}24
v8@?0
I16@0:8
@32@0:8@16@24
#16@0:8
Q16@0:8
@48@0:8@16@24@32@40
@56@0:8@16@24@32@40@48
@\"NSString\"
Vv16@0:8
v16@?0@\"NSTask\"8
no system bus AP present when expected
ret._release_gateway_control
AXchip_switch_taps
MantaMCUUpdater
Manifest authentication failed
not in xpc context
result.read_vals(portal_group)==
astris_exc_bread_test
gpr < 15
virtual int ARM7cpu_t::_halt_hw()
{%s=>%s} null reference to AXconn_t record, `conn`
 completed successfully.
mempool-size
group=%d
{%s} Failed to extract capabilitiesfrom table (%d); continuing anyway
[COLLECT] Halted. Status = %08X, DBGBREAK = %u\n
EXPLORE_JTAGAP
connecting to Ethernet probe
getOrCreateObject.messages
EXCEPTION(check) EXC(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s\n
[%s] error  reading EDSCR
AXdebug_auth_authenticate
generic error injected by probed
PROBED_LOSTCONN
MiscCortex
message
KalElBootService/BootServiceSecureBootStateMachine.swift
Existing firmware UUID: 
instr != 0
param.conn.user_defaults == NULL
internal.authenticate_dft.chip->soc == NULL
%s [RETRYING]
CreateParallelValidator
explore-level
True
{%s::%s} error %s writing EDRCR.CSE to clear EDSCR errors
couldn't read TCR
   {%s} After powerup CMDSTAT=%08X; debug domain is%s powered\n
.nonBlocking
DIGITAL_CERTIFICATES0
psu/MFR_REVISION
ret.reg.write.K_DA_REG_NAME_ECID1
regidx_restore=%u
UNKNOWN_CS_CODE
MantaMCUUpdaterCore/MantaMCUUpdaterCore.swift
AstrisProxy already closed.
retimer powered off
failed to create socket: %d\n
{%s} [%s] EDSCR with ITO set - unable to recover.\n
{%s} %s DC cache already clean since last halt, skipping flush
!!!! Critical Error: Failed To Initialized The CPU Object for %s with %s (%d)\n !!!!\n
AuthDebugWithTimer_t constructor - CIP_GEN_NUMBER 0x%08X\n
Failed to get PMU Name
{%s:%s@%d} [%s] doing IR scan (DTRTX INTEST)\n
UNKNOWN_DAPSTAT
ret.nonce_generation.timedout
Register file 16
m_num_high_pri_interrupts=%u
fn._ocd_reg_r.ddr.t1_save
fn.stmflash.h7.unlock_flash.write.cr1.key2
AXmemap_stmflash(_:baseAddress:buffer:eraseAll:quiet:)
bmcSerialNumberNotFound
service/ncm/enable
M4F
_set_bpaddr_hw
Requested Register Requires EL: %d - Highest EL: %d
{%s::%s} error %s writing EDSCR %s
{%s::%s} [%s] failed SW BP check [VA=0x%016llX, len=%d] (check=0x%08X, SW BP=0x%08X)
Flash Reg Adress is not set, using what is there\n
WindowStart
Crash level
Failed to unlock flash\n
astris_select_probe
{%s} strsep empty so match any probe [localhost]
{%s} %s
{%s@%d} astris_command: Astris Async: Error issuing async restart [%s]
illegalInput(_:)
AXbooster_interface_init_astris_api
nullptr == file_path_cfstr
result.ide==NULL
ret.getSubsystemEnableStatus
## ARM32cpu_t::read_register 64 bit 0x%x\n
param.ticket_data == NULL
OCD.DEBUGCAUSE = 0x%8.8X
rt13/12/pgood/1v2
Dart Name: %s\n
cpu-die
{%s:%s@%d} [%s] writing WVR %d\n
{%s} Unrecognized component: %08X, class %02X\n
ECID
Connected to Probe Map Server
end
{%s:%s@%d} [%s] PWR_VOSR read failed: %s\n
{%s} _pre_halt_hw result = %s
OFFLINE
AXdebug_auth_enable_timer_ovr
{%s:%s@%d} [%s] timed out waiting for CSYSPWRUPACK to be set\n
context.validators == 0
getOrCreateArray
 mcu firmware but got 
Trying to use size of 8 on not AXI bus
INVALID KIS VERSION
' VLAN interface already present (
getsockopt(socket:level:optionName:optionValue:optionLen:)
Using probe for marvin: 
Failed to get DFU Type
_write_internal
fn.AXmemap_read.address.regval
PORTAL_STS_MULTIPLE_BITS_SET
ASTRIS_ERR_TGTOFF
configuration()
init(query:)
Padded flash data with 0xFF from 
match-info
AXdp_read_with_recovery
{%s} 0 words from probe when %d words left to read for address 0x%016llX
/
ARMDAP
backupSRAMClearResponse()
j126CarrierSensor
Waiting for flash to idle after starting page erase, failed\n
ASC_ECORE_ROM
[%s] error reading EDSCR
[CLEANUP]\n
ret.reg.read.K_DA_REG_NAME_AP_DEBUG_EN
Too many data breakpoint regs (%u). Maximum is 2.
carrier/2/mcu/reset
CNIODarwin_CMSG_DATA_MUTABLE
sendmmsg(sockfd:msgvec:vlen:flags:)
We are at max iterations, still didnt get full JSON
KobaSWD
{%s:%s@%d} [%s] unable to read command response\n
.otherReadWrite
configured link local address for %s\n
Required key: %s @ index %d is NULL\n
_a64cpu_read_vfpreg_hw
v%s.%s
CortexA72
Size
No securityEpoch in options dict
connected(partnerChannel:myChannel:contextForInitialData:)
hostid
DOCK-CH-DATA
CPU.ARM
nothing written
astris_cpu_get_cl4_debug_signpost
register    %-15s %3u     \"%-s\"\n
Update RT13 success: 
[PCR][SWD]: id=%s(0x%X) - reg=0x%X (0x%llx) - reg_count=%d - val=0x%X
ACC
astris_ide_get_dbgwrap_base
INFO: %s(%04u): %s(): err=%s(%d): %s\n
R4
Register file 43
param.reg.invalid.outofrange
failedToConnectToRemoteService
com.apple.Manta.RetimerWatcher
KIS Readvals putting back the value
spsr_el1
(reg & (~(((((1U) << (2)) - 1) << (28)) | (0x40000000 | 0x80000000)))) < (sizeof(m_aarch64_msr_mrs_sysreg_encodings) / sizeof(m_aarch64_msr_mrs_sysreg_encodings[0]))
ret.read.ecid
{%s:%s@%d} [%s] Could not figure out flash size: %s\n
RF0
, powerButtonState=
didLoseTopologyGroup
rt13/0/pgood/0v855
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/booster_api/astris_boostermanager.cpp
Register file 4
fn.is_halted.setup_bp
(%s) %s
AXconn_create
IOInterfaceUnit
RestoreRTKitOS
    INFO(%u,%d): %s(%04u): %s(): %s: err=%s(%d): %s
{%s:%s@%d} [%s] \tFailure: only %u of %u write transfers were done (%s)\n\n
Expected data value for S32C1I
local host
KIS_DOCK
[%s] Booster System Is Not Initialized Bailing\n
IOServiceTerminate
preparePSUFWUpdateResponse(resp: 
Failed to reach 
Did Not Find Any Boosters For: %s \n
false
Die Addr Info: LSB: %d MSB: %d Len: %d Mask: 0x%016llX\n
{%s:%s@%d} [%s] writing ITR\n
Variables not setup
, boot2BSHA384: 
connecting to remote TCP socket at 
Process exited with nonzero return code 
Index is out of bounds
Match Count is Zero. This is invalid.
_read_register32
ret.drain.full-duplex
_handle_exception_for_el
dr <-
Writing START in FLASH_CR failed during page erase\n
{%s:%s@%d} [%s] executing LDCpi\n
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/astris_armv7mcpu.cpp
AuthDebugUseSSO
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/misc/astris_preferences.cpp
fn._ocd_reg_w.ddr.reg_val
Warning level
com.apple.private.MantaKit.mantahostd
Both debug and xbs versions are set, maybe a bug: %s
!!!! CPU Key %s is INVALID !!!!\n
\tReading left over chunk expected 0x%x got 0x%x\n
SoC not identified by IDCODE - enumerating instead of instantiating
MR3
Exc Cause: 0x%x - Exc Vaddr: 0x%x
at=%u,as=%u,offset=%u,opcode=0x%6.6X
manta-async-xpc-msg-unexpected-error
hasFixedWeakestLink
 failed to power on.
cpu-ascdebug-dbgack
dfu-Type: %s\n
{%s->%s} current EL (%d) already >= target EL (%d).\n
SoftwareBreak
AXcpu_lacc_status_insert
[%s] L2 cache params (when L2 via coproc): line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d
ret._a64cpu_read_gpr_cached
[Changing] Cached Raw: 0x%x Cached: 0x%x Expected 0x%x Old KIS: %s
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
 (eng)
Init objects failed
appendToArray.timing_phase
 in data source 
Image sections:\n
Invalid IP address: 
booster
_write_spsr
_set_halting
ConsistDbg
KIS_RSP_OK
SCNetworkProtocol
vlanDisplayName(_:)
NIOCore/NIOAsyncWriter.swift
psu/MFR_FWREV_SEC
SoC
--> cmd        addrsize=%d datasize=%d
ret.read.gpr_0
     0x%016llx: 0x%04x      %s\n
backupSRAMClearRequest()
pmu-name
cs_type:0x%x
AXcpu_lacc_pipe_set
AP[%d]: MEM_AP_APB\n
PARTNO_JTAGDP
_ocd_reg_dcr_r
Writing FLASH_CR1 failed during lock sequence\n
ioctl(SIOCIFCREATE): %d\n
{%s} no response from bridge
_write_general_reg_by_name
reset_connect_state
kisLoc
TCP send
APEXPLORE
\t[MATCH_APR] %s <= ((0x%08X & 0x%X) == 0x%08X)
RestoreOptions
{%s::%s} EDSCR error(s) |%s|%s|%s|%s|%s|
\t[MATCH_FOUND] identified chip: %s
cpu_hwbp_info
stream.h
current != kRegexInvalidRange
setResult
Perform OTA preflight
 can only get personalized RT13 firmware but got 
Invalid port number: 
AstrisRawTriage: Writing 
_a64cpu_read_sysreg_hw
[AstrisAsync][COMPARE] Error: NULL pointer(s) - acmd1=%p, acmd2=%p\n
Starting retimer watcher runloop.
astris_cpu_mmu_get_config
AuthDebugWithTimer_t::need_to_authenticate_probe super returned false; continuing \n
massErase
fn._write_special_reg
failed to read consistent debug root register, fabric may be hung
RSDComputeNodeBackend
transitionTimeout(to:
failed to create mach port to IOKit: 0x%x\n
RT13Updater/B2PMessageLogger.swift
internal.clear_probe_auth.debug_auth == NULL
tar
autoConfigure(_:)
 did not match expected seal byte 
implausible directory contents in 
Could Not Allocate Info Keys Array
dart-subsystem
[AstrisAsync] AstrisAsyncSyncGuard EXIT\n
{%s} hostname:%s, flags:0x%08x
Unable to get data from FTAB for '
%s%s\n
{%s:%s@%d} [%s] reading CPSR(2)\n
{%s:%s@%d} [%s] executing LDRpi(1,0,4)\n
{%s->%s} [aarch64] exec: encode_mrs(scratch=%d, MDDTR_EL0, %d)\n
Unable to read LR
{%s:%s@%d} [%s] FLASH_CR START write failed: %s\n
STM32F04x_FLASH
acquiringAndReleasing
 attempts, underlying error: 
[PCW]: id=%s(0x%X) - reg=0x%X - reg_count=%d - val=0x%X
CPU %s not found or already removed from the map
Failed to raise EL to %d to read register: 0x%llx
op_XSR_encode
value=0x%8.8X
failed to create log dump file
Connection inactive
new transition request 
Coprocessor coredump complete, corefile path: 
SPSR_ELx
astris_explore_ap_mem
EPC1
Misc register 3
Parse
Device already running other operation
APCIE_ANS0
{%s::%s} OSLK did clear (val = 0x%08X) [write_tries = %d].\n
{%s->%s} [aarch64] exec: encode_msr(MDDTR_EL0, %s=%d, %d)\n
probeNicknames
FLASH_PECR
\tWriting @ 0x%08llX...\n
Data break 0 address
com.apple.Manta.TriageController
AXcpu_hwwp_insert
\tLeft To Read (%d) < width (%d).\n
Table 5–137
var._tgt.invalid.null
addr_reg=%u,page_id=%u,data_reg=%u,opcode=0x%6.6X
Can't get hardware model - failed to convert to C string
ArcEM
AXconn_destroy(_:)
 fail, carrier is not present
After powerup CMDSTAT=%08X\n
result.read.memap.s2r_fsm
Misc_Rtx117x_t
firmwareVersion1
NIOAsyncWriterError.alreadyFinished
update(device:partition:firmware:)
unhandled error 
astris triage mode is not implemented
Accessing an ISA locked register (0x%llx), checking to see if any lock fields are set\n
disable
{%s:%s@%d} (ctictl[0x%08X] & CTI_CTL_GLBEN) != 0\n
setLockByteRequest()
Debug Clock Already Enabled
ExampleKey
Register file 49
fn.loop.xfer
ASTRIS_ERR_IFSTATE
SoC clocks are stopped. No MEMAPs allowed 
connecting to probe by port number
-----BEGIN CERTIFICATE-----\n
KalElBootService/BootServiceInsecureStateMachine.swift
Malformed manta-mcu-firmware-variant: failed to parse 
write.dspsr_el0 NOT CACHED
M33
internal.authenticate_probe.debug_auth == NULL
General register 10
fn._ocd_exec_instr.wsr.ddr.t1.1
carrier/1/present
AXbooster_print_boosters(_:pluginManager:)
 self-test fail, failure at step 
rt13/6/pgood/0v855
--> extrawrstn %d
{%s} %s status is '%s' [Status Read %d times]\n
Previous authentication in-flight, wait for it to finish\n
_write_window_base
astris_explore_enabler_get_cpu_status
AuthDebug_t::authenticate_probe failed (AuthDebugWithTimer_t)
Misc register 2
fn._ocd_exec_instr.xsr.ddr.t1.1
_write_mem
empty request encountered
#KIS
Failed to convert kisHubLoc %s to unsigned long long
IOInterfaceNamePrefix
IMAGE_SIGANTURE_512
rt13/4/pgood/0v855
fn.stmflash.g071.mass_erase.write.cr_reg
astris_batch_attitude_destroy
[AstrisAsync] Calling Complete Queue callback (%s) first_err %d last_err %d\n
\tReading left over chunk 0x%x @ 0x%llx\n
Probe removed prior to kick: probe %s
_rw_preflight
dest_gpr < 32
https://gs.apple.com:443
AuthDebugWithTimer_t destructor \n
Register file 23
Astris-%d.%d~%d
logger is NULL
set.probe_name
Installing handler for 
Testing carrier 
Could Not Create Dictionary From Booster: %s
_a64cpu_encode_msr
DEPC
MISMATCH
FACTSERNO
ParseObject
no items left in array
{%s:%s@%d} [%s] Reading FLASH_CR failed, when trying to unlock the flash: %s\n\n
ASTRIS_ERR_ANOMALY
[ANAMOLY] Could not find AXcpu_t object for CPU\n
%s: chip was NULL when attempting to release soc
s != 0
debug/forcepanic
Can't set retimer plug in 
error when moving file: 
MantaTriageController/MarvinTriage.swift
{%s} invalid data width %d bytes
\tLeft Over Chunk Read Failed\n
PARTNO_1176JZFS
RF61
PROBED_USB_REQ_NODEVICE
fn.stmflash.h7.mass_erase.read_optcr
kick
XPROG
CopyFrom
Failed to enable management network interface.
serviceID()
module/systemactive
batch_cmd_count: %d
Invalid APTABLE (%d), so using most restrictive
gor
astris_clear_user_die_select
' returned unsuccessful status 0x
AXcpu_hwwp_remove
ret.set_spmi_interface
{%s:%s@%d} [%s] FLASH_SR read failed: %s\n
Abnormal %s termination: Assert Area Mask = 0x%016llX
\tWriting 0x%08llX failed: %s
CPU (%s) has explore flag of: 0x%llx which is not set\n
BuildIdentityTags
vers_gateway < 2
_read_internal
%s - runBlock
MEVADDR
target power is OFF
addMember
)
result.astris_identify_load_booster
{%s:%s@%d} [%s] getting GPR (diff mode)\n
{%s:%s@%d} [%s] executing MOV\n
Register file 35
PlayerSWD
NIOCore/UniversalBootstrapSupport.swift
chassisTriageStart
armv7m-region-range
%s status is '%s'\n
{%s:%s@%d}\nFABRIC HANG DETECTED. JEBDUMP REQUIRED.\nContext: %s\nSoC: %s Rev: %s Address: 0x%016llx\nDescription: %s
RESPONSE_PAYLOAD_DONE
[1500] bridge '%s': tap %d does not match the plist's TAP entry %d
Failed to allocate space for table!
Invalid instruction breakpoint index %d
Toto
{%s:%s@%d} cmd_rcvd=%d is greater than sizeof(cscommand_t)=%ld [%s].\n
TLR
static_cast<std::ptrdiff_t>(sizeof(T) * count) <= (stackEnd_ - stackTop_)
critical
Failed to raise EL to %d to write register: 0x%llx
MAC16 data register 0
stderr
QueryInfo was called without an updater.
Failed to exec MSR to move contents of scratch (containing val to write) into sysregscratch=%d, sysreg=0x%X, val=0x%X, regname=%s
Unable to read PC
Table 5–188
Schema file is empty
CopyPart
debug/rt13swd/8_15
Malformed manta-mcu-firmware-variant bootarg count != 2: count 
fn.entry
!!!! Critical Error: batch attitude cannot be suspended when checking usage !!!!\n
CTI_OUT_EN0
sysreg=0x%X (%s), regname=%s val-> 0x%016llX
operation still in progress
INIT
{%s@%d} timeout waiting for DBGPRSR.OSLK to clear (prsr=0x%08X)
fc_ite_checks=%d
{%s:%s@%d} {%s->%s} EL3 not implemented\n
fn._write_window_base
NIOInsecureNoTLS cannot enable TLS.
AXbooster_print_loaded_boosters
{%s::%s} address=0x%08llX, length(in)=%d, width=%d, length(out)=%d, result=%s (todo=%d)\n
copyBoardNameForPrimate
## memapw %u 0x%016llX (%d) failed: err=%s, count=%d, status=%s, cmdstat=%x\n
ApProductionMode
FLASH_PRGKEYR
^^^^^^^^^^^^^^^^^^^^ DUMP OF HISTORY LOG ^^^^^^^^^^^^^^^^^^^^
, bootloader2BNonce: 
eraseSectorHandler(_:_:)
EDBVR0+index
   --> IDR: %08X\n
porpath
{%s:%s@%d} [%s] FLASH_PEKEYR write (first) failed: %s\n
COMPARE0
Clear requests in INTERRUPT
RF30
fn._read_general_reg
fn._ocd_reg_dcr_set.dcr_enable_ocd
Connected to Probe Device Server [Default Log]
NOP
CPU2
Invalid object or key for engineer array
warning
temp/front_middle
astris_remove_loaded_cpu_boosters
(crm & ~ARM64_HINT_CRM_MAX) == 0
{%s:%s@%d} [%s] writing CSSELR[L1-I]\n
fn._ocd_exec_instr.s32i.r1.r0
Port
setup_booster_soc
NIOCore/NIOAsyncSequenceProducer.swift
recvmmsg shim not implemented on Darwin platforms\n
result.read_vals(table_info)==
get_current_mmu_regs
defaults.nickname.not_connected
AXchip_getinfo
{%s:%s@%d} [%s] \tFailure: @ 0x%08llX failed to verify\n\n
fn._ocd_reg_r.dsr.regval_raw
Failed to save panic report: 
Failed to read CR reg\n
Switch back to primate KIS: %s\n
internal.authenticate.chip->soc == NULL
.start_time
com.apple.KalElKit
Debug (GitHash) version mismatched: %s (Expected: %s vs  Actual: %s)
CPU.ARMv6
{%s:%s@%d} [%s] doing IR scan (DSCR INTEST)\n
astris_user_default_set_boardname
fn.stmflash.h7.program.flash_idle
v8@?0
ObjectEmpty
service/rusb/status
nonceHashRequest
manta-async-xpc-msg-type
AXspmi_write_bus
Table 5–181
Xtensa Option options: 0x%x
GETSETTCK
newpos == 0 || path_[newpos - 1] == '/'
http://jmet-integration-ca.apple.com
Blink three times
virtual int ARMv7cpu_t::_halt_hw()
{%s:%s@%d} [%s] Waiting for flash to idle before mass erase, failed\n\n
XTENSAcpu_t
%@(\n
Calling get panic report for 
{%s:%s@%d} [%s] FLASH_CR MER read failed: %s\n
Xtensa Option non_tie_ranges: %zu range(s)
bp_index=%d
op_S32I_encode
_%04d-%02d-%02d_%02d.%02d.%02d
Waiting for flash to idle before sector erase\n
reset
param.conn==NULL
{%s} exec: DC_CIVAC_X1_ENC\n
{%s:%s@%d} [%s] FLASH_CR PG write failed: %s\n
fn._tie_read_word32.last
{%s@%d} Connection to server rejected, error=%d (%s)
start_time
rt13/2/pgood/0v855
read_dbg failed to access R_v7M_CLIDR
{%s} read %d words from probe when %d words requested
ARM11
Received error response for 
astris_explore_enabler_del_cpu
[AstrisAsync] AstrisAsyncSyncGuard EXIT: Preserving async state...\n
Reset
DEDICATED
RF45
{%s@%d} Probe response of %d payload bytes when local payload of %d bytes.
getOrCreateObject.diagnostic_checks
/usr/share/firmware/mantamcu/
ret.CFReadStreamOpen
{%s:%s@%d} [%s] PECR write (clean) failed: %s\n
High level 2 exception PC
fn._read_mem
fn._ocd_reg_r.OCD.DEVID
ASTRIS_ERR_PROBEEOF
EndObject
Retimers boot failed: 
handleIncomingData()
addEvent(event:)
set_or_replace
{%s:%s@%d} [%s] getting GPR 0 (diff mode)\n
no enable slot available
astris_memap_masked_read
enable_timer_ovr
AXbooster_print_boosters_detailed(_:pluginManager:)
unable to find IONetworkStack service\n
failed to enable network interface for service %s\n
{%s:%s@%d} [%s] error waiting for loader to complete: %s\n\n
{%s:%s@%d} [%s] timeout waiting for flash idle: SR = 0x%08X\n
_read_general_reg_by_name
Invalid data breakpoint index %d
ASTRIS_ERR_ISCONN
A firmware is already associated with 
ret.cfg.read.swd
Table 5–159
Table 5–170
LITBASE
fn.remove_epcn_epsn
AXconn_kick
{%s} unmodified-probe_match = %s
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/astris_arm7cpu.cpp
ICOUNT
Table 5–147
CNIODarwin_CMSG_DATA
ROOT_CERTIFICATES_1
explore_pid_swd
{%s:%s@%d} exception other than an abort or unknown (esr = 0x%08llx).  Don't know how to handle this...\n
Error while trying to authorize: %d - %s\n
ProbeNav
0123456789abcdef
--> wrstn_wir2 size=%3d dpcsoc=%d
{%s:%s@%d} [%s] executing VMOVW\n
ret.read.edscr.after-drain
Booster System Is Not Initialized Bailing\n
Error status from AMAuthInstallSetSigningServerURLPtr = %i
AMAuthInstallSetSigningServerURL
erase_page
AXI Error
--> debug      size=%3d acsr=%d
     ARM %s breakpoints: %u\n
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/cpus/astris_cpu.cpp
AXdebug_auth_get_timer_count
AXmemap_stmflash calling STM32F7xx::eraseflash\n
fn.stmflash.h7.reflash.flash_size
FlamingoSWD
{%s} %s: |%s|-|%s|
accept(descriptor:addr:len:)
AP[%d]: JTAG_AP (Exploring Later) \n
Table 5–138
_write_general_reg
op_RSYNC_encode
TAP-Only
relay_get: %s = %d
PrettyPrefix
com.apple.MantaAsyncXPC.MantaXPCListener.queue
j236CnodeSensors
ret.generate_nonce_and_send_request
Write Data Length Mismatch
timestamp
CertificateSecurityMode
%-16s @ 0x%08llX : 0x%08X\n
astris_ide_get_boardid
{%s:%s@%d} [%s] writing BVR %d\n
{%s} calling _collect_hw on %s
{%s} PRIMECELL [DONE]
Table 5–169
(data_.f.flags & kUint64Flag) != 0
, remoteDeviceName: 
{%s::%s@%d} [FALSE] src_reg[%d] < GPR_COUNT || == SP\n
AXcpu_hwbp_info
{%s} DEVARCH read fail in CoreSight component (%s)
Set Requests in INTERRUPT
!!!!!!!!!! Please enter the following commands to set proper permissions:\n
{%s} host = %s
default_schema_version is NULL
Booting retimers.
invalid hwinfo format: 
EXC_TRACE(exc_check): %s(%04u): %s(): %s: %s\n
     0x%016llx: ERROR\n
General register 7
address=0x%8.8X, regval=0x%8.8X
fn.stmflash.h7.unlock_flash.write.cr1.key1
connection about to be destroyed
Connection interrupted.
getValue(withTimeout:)
cpu-dbgwrap-status
{%s:%s@%d} [%s] executing STRHpi\n
PARTNO_SWDP_M0
FLASH_WRPR1
unable to transfer command to/from remote probe
Setting STOP CLOCK to TRUE
Test IOBoard pass
Test carriers present test, carrier(s) missing
rt13/2/pgood/1v2
astris_ide_refresh_boardid
High level 7 exception PC
Invalid bp = %u. Should be in range 0..1.
general-purpose failure
can't close selector gently as it's 
carrier/1/throttle
Had an error during transfer: %s
DEBUGCAUSE
locationids
AXbooster_get_loaded_boosters
{%s} Thread %#llx key %lu losing when not active for info %p - IMPLIED COP
CPU.ARM64
{%s} Batch attitude key created for %p thread %#llx key %lu
string_view::substr
Stale firmware running on device.
RestorePacket [bus=0x
ESR_EL2
FAR_EL3
param.width.invalid
param.bp_state.invalid.null
com.apple.KalElKit.UIServiceClient
sib-network-psr-reset
internal.clear-auth.debut_auth == NULL
Register file 12
kan
stack_.GetSize() == sizeof(ValueType)
astrisctl(args:)
!!!! Critical Error: aarch64[%d] == believed_64bit[%d] !!!!\n
ret.reg.read.K_DA_REG_NAME_AUTH_TIMER_COUNTER2
MemberCount
updating(blockNumber: 
development
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/booster_api/astris_boostermanager_soc.cpp
dart-type
ApSecurityMode
New Length: %d\n
relay_set: %s -> %d
TagNumber
Attempting to connect to [
Register file 11
BLK
MantaComputeNodeDescriptor(udid: 
OCLA_IP_REGS
Original Length: %d\n
AMAuthInstallSupportDictionarySetInteger32
remove()
manufacturingDate
com.apple.KalElKit.FactoryDataServiceClientChannelHandler
_Concurrency/arm64e-apple-ios.private.swiftinterface
known-constant allocation
Programming (addr: 0x%08llX) Failed!!!
ret._a64cpu_get_current_el_hw
DEBUG CLOCK OFF
SCNetworkService
Cannot perform vector reads on this operating system
AXcpu_mmu_get_mair
En masse...\n
General register 9
^^^ *** PREVIOUS ASTRIS SAW A HANG *** ^^^\n
{%s} probe [%s] added to list
Misc_Rtx117x
rt13RestoreRTKitOS
debug-size
     ARM %s debug CPU rev %d\n
{%s:%s@%d} [%s] PECR write (clear) failed: %s\n
EPS2
MiscCortex_t
com.apple.KalElKit.SignalServiceClientChannelHandler
Found another target for the plist\n
ret.chip == NULL
Preferences does not exists: %s, creating one.\n
COMPARE1
Table 5–178
Unable to setup VLAN on 
wrstn-pipes
STM
{%s:%s@%d} [%s] timed out waiting for reg_index %d to equal: ((0x%08X & 0x%08X) == 0x%08X)\n
PARTNO_DAPLITE
Invalid parameter exec_path = %d
Die-Count: %d Current-Die: %d Die-Type: %d
ARM64cpu_t
ret.dspsr_el0
ret.reg.write.K_DA_REG_NAME_ENABLE_PKA_VALID
Awaiting response from Probe Map Server
CERTIFICATES_CHAINS_2
rt13/14/pgood/1v2
UserCreated
writeBlock(flashData: 
AXmemap_read64(desc) failed
ret.reg.read.K_PKA_REG_NAME_DBG_VERSION
Please file a radar (Astris | all) describing the issue\nand attach a sysdiagnose from this machine.\n
SOC
{%s::%s} [%s] secondary error %s resuming permission checks [VA=0x%016llX]
Stop Clock Active
enable(_:)
MantaXPCInternalService
FLASH_ACR
User created bundle found, ignoring version checking via plist
NXP
!!!! Critical Error: Took an exception that took us to exception level[%d] other than 1, 2, 3? !!!!\n
_a64cpu_lower_el_hw
L1 icache
Buffer does not contain a value for tag 
vlan
[AstrisAsync][COMPARE] MISMATCH: cs_type - acmd1=0x%04X, acmd2=0x%04X\n
AXcpu_lacc_count_insert
Type 'jebdump -chip %s -rev %s' to do scan/mem dump\n
fn._ocd_reg_r.dsr.dsr
Standard level
probe matching %s on host %s
Complex Name: %s\n
setway_reg
_init_bpwp
AuthDebug_t::authenticate failed (AuthDebugWithTimer_t)
%s.%s.%s
ChimpSWD
GETRELAY
cpu_lacc_count_clear
rt13/11/pgood/0v855
failed to name network interface\n
RPM
va
     0x%016llx: 0x%08x    %s\n
defaults.board.not_connected
Going To Create Generic ARMV7m, but typehint is present (%s)\n
[INIT]\n
first stage bootloader
MultiThreadedEventLoopGroup { threadPattern = NIO-ELT-
didDiscoverTopologyGroup
init(logger:group:listenOn:tcpConnection:ipAddressTags:)
New format for cip gen register, unsupported: %d\n
Found probe memory transfer in progress; clearing EDSCR.MA.\n
copyNicknameForPrimate
Cycle count
value
failedToConnectToRemoteService(remoteService: 
fn._write_window_base.wb_save
unable to create connection
Failed to create CPU %s - %s\n
Empty
GenericValue
enableRetimerPlug
elr_el2
Table 5–171
fn._ocd_reg_dsr_w.dsr_status_to_clear
address=0x%8.8X,page_id=%u
_tie_write_word32
checking if relay \"%s\" is valid
CLOSE
SWD
UNKNOWN CODE
GEN
Fatal error
device is in panic state
Unexpected sequence number 0x
Programming Error is Set\n
{%s->%s} [!aarch64] exec: encode_msr(MDDTRTX_EL0, scratch=%d, %d)\n
_ocd_exec_instr
(Last: %s)
ARMV4
update, bundle: 
productionStatus
Current chip revision = 
Unknown button state 
UNKNOWN CMD
Info_
cpu-dbgwrap-offset
astris_ide_get_bootid
%@,ProductionMode%@
posix_spawn failed: 
%s constructed
{%s:%s@%d} [%s] reading SPSR\n
_get_bpaddr_hw
[AstrisAsync] Got ASYNC_RESTART response!
EXPLORE_JTAG_NO_BOUNDARY_SCAN
{%s:%s@%d} [%s] busy timeout on lock (out): %s\n
_a64cpu_read_gpr_cached
Couldnt figure out the size of flash (we read: %d), using default\n
RF8
HOSTID=0x%x which is invalid, skipping orientation check
EPIWRITE
cpu_cleaninv_dcache
no options supported
SignalServiceMessage(header: 
get(_:for:personalize:)
Values Not The Type We Expected. Expected: Number and String\n
astris_jtag_scan_stay_gotorti_impl
fn._ocd_reg_r.ddr.regval
_insert_instr_breakpoint
STM32Hxxx
Apple connect client internal error with code 
dataBlock(blockNumber: 
Requested firmware version: 
{%s} no matching 1500-to-* bridge
{%s:%s@%d} [%s] Writing PG to FLASH_CR during programming failed: %s\n\n
{%s:%s@%d} [%s] \tFailure: only %u of %u read transfers were done (%s)\n\n
EPS5
more than one when unique required
j236InternalCables
startingHeartbeatHandler(_:_:)
{%s} [%s] EDSCR with ITO set - ERR while waiting ITE.\n
ret.read.edscr.masked.beginning
HardwareStep
AXspmi_read_bus
AXmemap_stmflash calling STM32F2xx::eraseflash\n
SEQ-ID=0x%X - SWD-SUB-CMD-ID=0x%X - SWD-SUB-CMD=0x%llX
ChannelPipeline[
Ignoring device with unknown identity.
Size or Count provided are 0.
{%s} [EDSCR_RXFULL !is_64] exec: encode_mrs(0, MDDTRRX_EL0, false)\n
response == NONE; failed to get kis target info\n
 is missing, input 
Failed to cleanly disconnect: 
{%s:%s@%d} [%s] {%s} port[%u] specification no longer supported\n
  non_tie_ranges[%zu]: base=0x%08X size=0x%08X name=%s
_insert_breakpoint
mismatch detected
\tFailure: only %u of %u read transfers were done (%s)\n
ParrotSWD
Failed to instantiate %s\n
Select == %d
        JTAG-AP, port %u: Found %08X Chiphandle %04X, IR:%d/%d, DR %d/%d\n
Device heartbeat check-in.
Selecting
storeNicknameForKey
fn._insert_data_breakpoint
param.op.AXCPU_WP_DISABLE.unsupported
{%s} couldn't set thread specific - %s\n
Probe (port=%d) with unknown status %s dropped from available list
temp/exhaust_air
writ
ret._set_wpcr_hw
## armcpu: success status even though not all bytes read\n
[INSBP] bp%d addr=%08llx ibreakenable=%08X\n
astris_kis_get_bypass_info
{%s:%s@%d} exception other than an abort (esr = 0x%08llx).  Don't know how to handle this...\n
VERSION
psr-bit
AXcpu_readreg_vals
ParseRange
LoggingExtras/MantaLoggingSystem+SignalHandling.swift
astris_ide_print_platform_info
EDDTRRX
????
cio/grp1/0/cable_present
Unable to get existing firmware version: 
Table 5–173
dispatchQueue(_:)
https://gg-dr.apple.com:8443/ca/certify
Decoding error: 
, sectorOffset: 
{%s:%s@%d} [%s] writing BCR %d\n
CLIDR
couldn't read TTBR0
      Select port %u: PSTA=%08X CSW=%08X [%s]\n
tckrate_check returned error %s
Expected to decode UInt8 but found a 
swdovrrun
** Network Error & Using SSO. Please check you are signed into AppleConnect.          **\n
[PREFS] Key: %s - Val: NULL
Register file 56
Unique required when multiple probes
AXap_by_type(_:type:)
{%s:%s@%d} [%s] executing MOV (diff mode)\n
%d > %d
MantaKitComputeNodeProxyRUSBTrafficV2
Table 5–177
## armcpu: Didn't write the right amount: wanted %u got %u (%08llX-%08llX)\n
internal.enable-timer-ovr.debut_auth == NULL
AXmemap_stmflash calling STM32L4xx::reflash()\n
ROOT_CERTIFICATES_2
\n!!!!! Unable to obtain lock while initializing default logging !!!!!\n
debug/carrierkanzi
previous next 
AXportal_t Struct Is NULL
write.reg.not cached
m_bp_details
ACQ_SAMPLE_SPI
MAIN_DEBUG_ROM
result.read_vals(group0)==
\tAligning memap access width. New Chunk: 0x%x @ 0x%llx Left Over %x\n
Product Name: 
RELAY
astris_json_set_address
!!!! Complex CPU Key %s is INVALID !!!!\n
_is_bpwp_initialized
Unable to disassemble_at_addr 0x%016llx
ret.pka.nonce.status.err
STM_FLASH_KEYR: 0x%x\n
setTargetOS
check_for_flash_error
RF16
carrier/2/mcu/ready
{%s} cleaning/invalidating coprocessor-register-controlled L2 cache (sets=%u, ways=%u)
IBREAKA0
ICOUNTLEVEL
MISC2
errorCaught(context:error:)
Channel user inbound event 
{%s=>%s} null reference to AXchip_t[0]
{%s} probe_match = %s
IsValid()
from != 0
getDevices()
param.op.AXCPU_WP_ENABLE.unsupported
\t[MATCH_APR] %s <= AXap_read(ap, 0x%08X, &value)
 didChangeFromState 
{%} exec: encode_hint(NOP)\n
startApplication
{%s::%s} EDSCR with RXO set - unable to recover.\n
[%s] {%s->%s} Transitioning %u -> %u exception level.\n
DSR
stat(pathname:outStat:)
Interrupted while fetching retimer info: 
SoC has been setup using standard instantiation (setup result=%d)
currentWeakestLink
Required Key-Value is a string, and not an array. Old booster found: %s\n
DFR0_LO
ret._setup_wp
shared_ != 0
{%s} %sing word #%d at address 0x%09llx: %s
fn.stmflash.g071.mass_erase.read.cr_reg.before_start
ret.write_sysreg_hw.spsr_el
hwwp_disable
digestInfo is missing
 is not supported on this platform.
Nonce
[KIS] CMD: %s \n
Complex Address: 0x%llX\n
high word
Unable to connect after multiple attempts:\n%s,\n%s
GetHashCode
channel inactive
Enabling power supply on outlet 
extract
KIS Chip Found, Doing KIS Explore Setup
ret.astris_create_cstr_from_cfstr
general error reported by probe
update(device:application:boot2A:boot2B:)
** Unauthorized User/Network or ECID **\n
PARTNO_SWDP_M0P1
read_dcc
Misc_CortexM
NIOThread(desiredName = 
rt13/6/pgood/0v805
   Debug Port has unknown type\n
astris_findidcode
GetState
explore_min
latching: EL%d
lower.safe.aarch32=notsupported
No chipRev in options dict
init_hw.pid0
no AP (Access Port)
ASTRIS_ERR_BADPARAM
spmi
Apple
!!!! Critical Error: Nested exceptions... get someone to debug this. !!!!\n
Optional Key: SubsystemMonitor not in preferences
ProductBuildVersion
getDigestInfo(device:)
udid info 
% PWM is running at 
{%s} a=%09llx d=%016llx v=%llx u=%llx r=%llx s=%llx w=%llx
{%s::%s} NULL parameter
RF33
buildCategoryJson
n >= 0 && n <= 308
internal.is_dft_authenticated.chip == NULL
invalid environment variable
param.portal.dcm == NULL
{%s} Unable to read SP_EL0
PowerGated
Table 5–154
Failed to get panic report for kalel 
param.regval.null
ret.reg.write.K_DA_REG_NAME_NONCE_2
Error - STM32%s reflash failed (%s).\n
High level 3 exception PC
StringEqual
securityEpoch
Algorithms/Compacted.swift
dcm
ASTRIS_ERR_PENDING
AstrisSWD
Ignoring reboot response error: 
symbol.check.loaded.AMAuthInstallRequestSendSyncPtr == NULL
fn._reg_desc_lookup_by_name
operation not supported
--> wir        size=%3d wirshiften=%d wrstn=%d dpcsoc=%d
misc-wirtestporten
pc:  0x%16s cpsr: 0x%16s %s\n
no SOC object available
schema_version
Probe Map Server Information: %s
userInboundEventTriggered(context:event:)
Cached async_replay capability version: %u
{%s::%s} cpu powered off: failed init() %s
symbol.check.loaded.AMAuthInstallSupportDictionarySetBooleanPtr == NULL
Failed to convert CFArray to C Array\n
name(_:)
taps
RF25
Proxy close error: 
dart-name
L4xxx
Exception virtual address
sending abort to clear a timeout\n
, boot2BLength: 
SigningFuse
Unknown board type
write.dlr_el0 NOT DIRTY
STM32F07x_FLASH
op_L8UI_encode
addError
Invalid IPv4 Address 
XPCRemoteConnection()
{%s->%s} current EL (%d) already == target EL.\n
astris_dpabort
plist
AXI-ERROR=0x%X - AXI-XACTION-FLAG=0x%X - ADDRESS=0x%llX
value doesn't fit in UInt32
CIP Gen Number: 0x%08X - Major: %d Minor: %d\n
WP Settings incorrect: wp%d addr=%08x mask=%08X\n
RF26
Timeout waiting for flash idle: SR = 0x%08X\n
Attempted to decode Never
param.no_ap
_NIODataStructures/Heap.swift
CPU Supported in Integration: %s\n
Complex CPM Offset: 0x%llX\n
{%s} Failed to extract chip  revision/board ID from table (%d); continuing anyway
[RESUME] Chip %x\n
AXcpu_sstep
Failed AP write of R_MEMAP_CSW res: %i newval %i
check_timer_and_clear_timeouts
Invalid socket address: 
Failed to receive response for request before deadline
read memory
{%s:%s@%d} [%s] Writing page address to FLASH_AR failed during page erase: %s\n\n
/tmp/command-stdoutput-
[%s] {%s->%s} END handling exception
ret.clear_dft_authentication
AuthBase_t::load_framework failed
RTKitOS
## armcpu-r: %s 0x%016llX (%d bytes) -> 0x%08X\n
Async is disabled for current seesion
Invalid reg_index %u
target not in appropriate state for action
%s_probe
services()
carrier/1/mcu/ready
[AstrisAsync] Discarding %zu completed command(s)\n
astris_cpu_mmu_configure
cpu_writemem
Acdcuc
RSM
{%s} [%s] m_exception_level=%u\n
[%s] L2 cache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
{%s:%s@%d} [%s] Read DWT Comp %u\n
PARTNO_ARM7TDMI2
RF53
_read_general_reg
Client connected
CCSIDR
get_mair
ret.reg.read.K_DA_REG_NAME_AUTH_TIMER_ACTUAL_LOAD
Table 5–184
param.as.invalid.>15
armv7m-region-type
astris_user_default_copy_nickname
Going To Create Generic ARMV8\n
 bytes>, payload=<
SeekOrigin(rawValue: 
getEthernetInterfaceForParent(interface:ancestors:)
SelectableEventLoop { selector = 
Beginning of set
{%s} bridge returned DECERR
CPU Monitor key does not exists for: %s\n
RF40
fn._ocd_reg_r.DDR
{%s:%s@%d} [%s] executing STCpi(uint32_t)\n
Failed to enable retimer plug :
{%s:%s@%d} [%s] writeval: %s\n
Unable to allocate memory for next part of big response
haskis
_halt_hw
nullptr == soc_bm
PushBack
vlanPhysicalInterface()
offset element 
failed to setup vlan %s\n
Group=%d start=0x%llx count=%d soc_addr=0x%llx\n
MantaMCUUpdaterCore/UpdateRT13.swift
this must be overridden by sub class
   Debug Port: SELECT %X; error: %s, retrying..\n
AXdebug_auth_set_sso_user
STM_FLASH_ACR: 0x%x\n
RF36
Deactivating handler
\t Writing 0x%08llX...\n
Register file 19
fn.stmflash.h7.sector_erase.flash_idle.after_sector_erase
{%s:%s@%d} [%s] doing JTAG scan (DTRRX data)\n
readFactoryDataRegion(key:)
Algorithms/FlattenCollection.swift
Invalid file name: \"%s\". File names must not start with '.'
PMGR_OCLA_REGS
{%s} [is_64] exec: encode_msr(MDDTR_EL0, 0, %d)\n
 RPM, faster than the expected maximum 
com.apple.Manta.SCDynamicStoreQueue.
NIOThrowingAsyncSequenceProducer allows only a single AsyncIterator to be created
Literal base
Register file 17
invalid host name or port
!!!! Critical Error: suspended batch attitude thread trying to lock - CAN'T LOCK !!!!\n
{%s:%s@%d} [%s] std::copy failed: %s\n\n
rt13/1/pgood/1v2
dbgarch
   {%s} Probe requires overrun detect mode.\n
str != 0
products_
close_flash
RF12
cpu_hwwp_disable
dspsr_el0
internal.authenticate_probe.chip->soc == NULL
_init_configuration
SOC_t::{%s} null reference to AXcpu_t record, `cpu`
!!!! Critical Error: current_el[%d] <  %d !!!!\n
astris_user_default_copy_nickname_for_key
MAC16 Data register 0
Invalid port[%s] for probe %s provided by probe server
can't register on selector as it's 
Invalid GPR Given: %d > %D
{%s::%s@%d} [FALSE] base_reg[%d] < GPR_COUNT\n
Failed to receive response for request before deadline.
explore
{%s:%s@%d} [%s] Error - %s\n
{%s:%s@%d} [%s] \tCould not unlock flash\n\n
createConsoleServer(consoleType:inputHandle:)
Retimer runloop failed: 
Error happened when reading edscr. Retry #%i\n
!!!! Critical ERROR: current_el[%d] != m_exception_level[%d] after exeption handling
[AstrisAsync] REPLAY DIVERGENCE: completion cache mismatch!\n
Reading FLASH_CR1 failed during unlock sequence\n
rt13/12/pgood/0v805
MantaRetimerController/Retimer+PublicAPI.swift
fn._init_configuration_by_name.failed
MemberEnd
smc
DCRCLR
Parent key is not an object
kern.bootargs getsize returned 
entryCreateProperty(propertyName:)
astris_create_ap_slave
The log file has been updated with all available diagnostics.\n
Invalid Bundle: %s
fn._ocd_reg_w.dcrclr.regval
FLASH_CR1
getsockname(socket:address:addressLength:)
setLockByteImpl()
bpcr
Loop-begin address
GetUint64
astris_batch_attitude_suspend
[%s] %d -> %08x\n
BYPASSCH
clzll.h
class_var.m_interface_name==NULL
AppleANS2NVMeController
NIOThread(name = 
rt13/4/pgood/0v805
master-localwrstn
{%s} GENERICIP: name=%s, base=0x%llx, type_hint=%s
High level 5 exception PS
RemoveDotSegments
lock()
firmwareUpdateStatusRequest(firmwareSelect: 
unpack_response
tagNumber
_clean_dcache_vaddr
ServerSocketChannel { 
{%s:%s@%d} [%s] reading WVR %d\n
FLASH_WRPR3
{%s:%s@%d} [%s] SR read (status) failed: %s\n
{%s::%s} creating CPU
[ARM32cpu_t::_update_register64] 0x%08x\n
entryID()
Value Types Are Not Strings\n
Invalid category name
gmtime() returned NULL, using epoch time
cpu_swbp_remove
BootedOSOSUpdateStrategy
NIOPosix/SelectableEventLoop.swift
{%s} Thread %#llx clearing key %lu
open(file:oFlag:mode:)
complex-cpu-id
!!!! Critical Error: m_current_rw_is_64[%d] && reg[%d] < GPR_COUNT) || < 15 !!!!\n
{%s:%s@%d} [%s] busy timeout before open: %s\n
*
Expected to decode Optional<()> but found a 
D0-PKA
{%s} DAP command nwords=%d trimmed to %lu\n
ASTRIS_ERR_NOTFOUND
Swift/NativeDictionary.swift
   JEDEC ID: 0x%08X\n
BananaSplit
cpu_status
fn.stmflash.h7.sector_erase.read.cr_reg.before_start
FindMember
SOC AP[%d]: JTAG_AP\n
u32toa
Master BoosterManager
fn._return_from_debug_interrupt
  Error path [%s]\n
getNANDStorageInfoFromIORegistry()
writeRead(_:sequenceNumber:)
 is above maximum length 
all
_get_bpcr_hw
cpu_mode
{%s:%s@%d} Critical error [radar already requested]
PROGRAMMABLE_HW_FW2
[1500] No %s.plist resource found
set.target_os
Failed to create hardwareInfo, options: %@
Unexpected opcode '
OK: address translation resumed for %s successfully
No 1500 bridges or TAPs specified (v2 plist)\n
{%s@%d} {%s[writev]} %d(%s) [RETRYING]
Could Not Match A Booster for %s\n
Register file 5
Writing KEY2 During Unlock Sequence Failed: %s\n
Failed to open schema file
product-name: %s\n
Failed to restore EL to %d after reading register: 0x%llx
Failed to write reg_addr=0x%llx val=0x%llx
Failed to %s halting debug to on CPU: %s with %s. Will retry on next power-on.\n
MEPS
JTAG chain not yet explored
Malloc
com.apple.Manta.MantaMCUUpdater.RequestChassisReset
[%s] L1 dcache params initialized: line size %d bytes, sets %d, ways %d, wayshift %d, lineshift %d\n
address =0x%X is too large for 32 bit unsigned.
no error
{%s} Found extra info in = %s, chopping string
kob
JsonLogger: Loading schema for category '%.*s' from '%s'
MCUHardwareInfo(chipId: 
failed to create dgram socket\n
{%s::%s} [%s] error %s from _synchronize_context.
_a64cpu_clear_async
ExcCatch
Unable to encode flash service message to byte stream: 
retimerStateUnknown
Clear (1<<1)
CPU.ARM7
AXmemap_stmerase
fn._ocd_reg_w.ddr.address
%@,ChipID%@
.otherExecute
PendingStreamWritesManager { isFlushPending: 
udid event 
MantaKalElController/KalEl+ConsoleProxy.swift
DBGCTRL = %08X   res=%d\n
var.bp_index.invalid.outofrange
Skipping restricted address read: 0x%llx (in range 0x%llx-0x%llx)
SoC BM Not Found, Bailing\n
Prefix
0123456789ABCDEF
fn.missing_entry_function
{%s::%s@%d [%s]} Error %s: cleaning and invalidating dcache vaddr: 0x%llX
Unable to decode flash service message from byte stream: 
module/systemreset
{%s:%s@%d} [%s] scanning out (DIDR)\n
DBREAKC1
DefaultConnectAddress
PriorityQueue(count: 
Failed to boot into selected stage
handleOutgoingData()
dr-length
EDPRSR_AON
## apw %u 0x%08X 0x%08X\n
probetimeout retrying access...\n
fn._read_snr.exccause
[Typehint] Values Not The Type We Expected. Expected: String & Array or String & String\n
CPU.ARMv7m%s
TOOMANY
Response incomplete
[1500] Error parsing IR command: %s
Die Addr Info LSB: %d Mask: 0x%016llX\n
ResponseTags
failed to copy network stack service\n
AXlog_init_with_ctx: lock could not be obtained
maxAPBCount set to 
DoubleWord(high: 
resettingHandler(_:_:)
{%s} Failed to extract target ID from table (%d); continuing anyway
 MCUs, iteration 
Update Compute SMC proxy: 
Not supported portal of type: 0x%X
{%s} [is_64] exec: ISB_SY_ENCODING\n
Memory error PS register
set.os
result.extract_version==
{%s} status=%d being reported as Unknown
com.apple.Manta.SerialConsoleClient
Discovered device 
{%s::%s@%d} [FALSE] system_reg[0x%08X] & SYSREG_TYPE_MASK != 0\n
{%s:%s@%d} [%s] write to CMD/STAT failed\n
Reading FLASH_CR2 failed during unlock sequence\n
cpu_lacc_status_insert
Saving paniclog for 
Hardware test failed
rt13/9/pgood/0v855
AXportal_reset_dcm
carrier/1/mcu/reset
Connection closed
SWD_BYPASS_REGS
{%s:%s@%d} [%s] timed out waiting for: ((0x%08X & 0x%08X) == 0x%08X)\n
authenticate
Unexpected locked status value 
PPM
{%s::%s} [%s] WP_REMOVE m_wp_avail=0x%X, m_wp_rsvd=0x%X, index=%d
ret.write_reponse_and_check_authentication
fn._ocd_exec_instr.l8ui.r1.r0
Writing KEY2 During Unlock Sequence Failed\n
AXbreadcrumbs_clear
Device is production fused
[%s] Booster System Is Not Initialized\n
15002APB
{%s::%s@%d} [FALSE] dest_gpr[0x%08X] < GPR_COUNT\n
param.regval.invalid.null
astris_explore_enabler_get_subsystem_status
   Debug Port: Trying SELECT %X\n
arm-io
getHasGpu(chipRev:)
Testing chassis fan 
{%s->%s} exec: encode_msr(%s=0x%X, scracth=%d, %d)\n
edscr: 0x%08x - el: %d (Current EL in Debug State)\n
xfer_acmd_via_sock
Powering up retimers.
var.bp.invalid
http://jmet-integration-ca.apple.com/fdrtrustobject
R
param.m_ap == NULL && param.m_lam == NULL
superEncoder(forKey:) is not supported for XPC encoding and Codable still doesn't throw from this method
!!!! Critical Error: Restoring from exception level[%d] other than 1,2 or 3 !!!!\n
port_%d
cpu_get_cl4_debug_signpost
unable to open IONetworkStack service: 0x%x\n
cpu-xtensa-ocd-base
{%s::%s} Unable to locate register (offset 0x%08llx) in memory block
Disabled
fn._read_snr.excvaddr
{%s} handle ROM entry
{%s[select]} timeout while waiting for data from the connection
Pow10
Retimer setup complete.
.otherRead
 successfully enabled.
    INFO(%u,%d): %s(%04u): %s(): err=%s(%d): %s
\tCould not get sector number for address: 0x%llX\n
op_S8I_encode
testMellanoxFan()
get_soc_resource_filepath
General register 5
socTriageDataReady
Channel had no remoteAddress
[KIS] Words (Read/Write/Wrote): %d\n
[%s] error reading EDSCR with mask
   Debug Port: SELECT %X: DISABLED\n
\tWriting 0x%X bytes @ 0x%08llX...\n
buffer != 0
MantaMCUUpdaterCore/SetupIOBChildren.swift
ELR_EL3
{%s} Component ID read fail for 0x%llx (%s)
{%s:%s@%d} [%s] second read of CMDSTAT failed\n
Could Not Find Bank (%d) For Address: 0x%08llX\n
AstrisRawTriage: Wrote 
!!!! Critical Error:  dlr_el0 NOT DIRTY !!!!\n
opcode=0x%6.6X
PushUnsafe
{%s::%s} [%s] WP_ENABLE _set_bpwp[%d] failed (%s)
ByteBuffer { readerIndex: 
name
name()
read(descriptor:pointer:size:)
channelInactive(context:)
result.read_vals==
_write_memory_fast_try
[ADDING M3 REGION] base=%llx range=%llx offset=%llx type=%d region=%s\n
Failed to setup wp=%d
XPCObjectEncoder or XPCObjectDecoder is required to encode or decode this value: 
spr-regs
{%s:%s@%d} [%s] writing SPSR\n
ELR_EL2
DBREAKA0
com.apple.Manta.BootServiceMessageRouter
personalizationRequest
soc-pid
Dumping Process Tree
Unspecific syntax error.
event
fn._read_special_reg.reg_srn
shift=%d,opcode=0x%6.6X
 signature value: expected 
[AstrisAsync] Discarding response due to ASYNCSKIP state!
_gen_debug_interrupt
Probe %s Device Not Connected on USB-C Port
generated_files
Dropping response due to previously encountered error
Connection invalid.
{%s} read[ED64] of %s @ address 0x%016llX = 0x%016llX
update(bundle:): ecid=
Invalid value for 'entry' tuple element - can't index
Map is empty, not removing CPU %s
ASTRIS_ERR_IGNORED
[INSBP] bp%d addr=%08llx fpr=%08X\n
{%s::%s} [%s] Error determining if any breakpoints or watchpoints set
AXcpu_readmem
fn._ocd_exec_instr.rfdd
GetDouble
operandStack.GetSize() >= sizeof(Frag) * 2
Unexpected request
cio/grp0/1/cable_present
sel-sib-network
ret.clear.edscr-error
CPU[%s] Write Reg: %d Val: 0x%llx
_read_cpu_reg_file
ASTRIS_ERR_PROBED
no debug bus AP present when expected
## apr %u 0x%08X -> 0x%08X\n
astris_json_logger_to_json_string
Acdcuc3
APB Capability does not exist.
T32
fn.__ocd_reg_w.ddr
received %zd bytes from Probe Map Server when have %zu
{%s:%s@%d} [%s] reading PRSR (!lsr)\n
Initialized %d 1500 bridges\n
_get_arch_hw
param.addr_reg.invalid.>15
com.apple.Manta.MantaFirmwre
Sending command: 
(reg & (0x40000000 | 0x80000000)) != 0
{%s:%s@%d} [%s] FLASH_CR SER read failed: %s\n
data_.f.flags & kUint64Flag
externalDeviceProxy
 to collect core for 
_a64cpu_read_edscr
https://fdruca.apple.com:8443
Received info about 
Could Not Get Bundle Out Array of Found Boosters\n
init_hw.read.dhcr
/Library/Caches/com.apple.xbs/95DA7A4B-640D-4D28-B02C-FC42D0EA9EF7/TemporaryDirectory.4pgkhs/Sources/AstrisArmProbeServer/api/debug_components/astris_dapcmds.cpp
(width == 1) || (width == 2) || (width == 4) || (width == 8)
fn._write_special_reg.dbreaka1.address
bad parameter(s) specified
Failed to get file descriptor from xpc_fd.
SerialLog/SerialConsoleClient.swift
Subscribing to signal 
[KIS] Portal Status: 0x%X\n
ERR
L1_DATA
Cleaning up Each Booster Manager\n
!!! Failed to find a required key for product: %s dfu:%d pmu:%d !!!\n
Invalid file name: \"%s\". File names must be at least %d characters long.
{%s::%s@%d} [FALSE] dest_reg[%d] < 15\n
bridgeDisplayName(_:)
http://jmet-integration-skyline.apple.com
fetchRetimerHWInfo(retimer:)
 (%s)
module/pafsha256_boot1
!!!! Critical Error: suspended batch attitude for info %p trying to cop - NOT ALLOWED !!!!\n
{%s:%s@%d} [%s] doing IR scan (DIDR SCAN_N)\n
AXdebug_auth_is_authenticated
fn._ocd_reg_w.DIR0EXEC.instr_32
dbgfifo
 as MantaMCUFirmwareVariant.
SP_EL0
[CMD] %02u:%02u:%02u.%06u|%s <%s> %s
Low level
ASTRIS v%s%s [%s]
Failed to find symbol for %s in downstream at path %s. This might be OK.\n
base
dpb-size
{%s::%s} creating placeholder for CPU: name=%s
KalElFactoryDataService/FactoryDataServiceMessageLogger.swift
cpu-group
{%s::%s} [%s] error (%s) getting number of HW WPs
{%s:%s@%d} [%s] Buffer data to RAM failed: %s\n
STM_FLASH_OBR: 0x%x\n
fn.stmflash.h7.wait_bank_flash_idle.timeout
XACT
%s,%s:l=%u,c=0x%X,i=0x%X,f=0x%X
 bytes) does not contain enough data to deserialize value of type 
connectingSignalServiceHandler(_:_:)
Start Page: %d\n
getpeername(socket:address:addressLength:)
com.apple.Manta.MCUTracer
{%s::%s@%d} [FALSE] OP2 out of range [0x%08x]\n
AXarm7_dbgread
connecting to selected probe
performing direct connect by port number
connectingSignalService
TBMLocked
   %s target on AP Sel %u; address = 0x%llx id = 0x%06X type = %d\n
Address formatting failed
SocketChannel { 
Badly formatted request.
{%s:%s@%d} [%s] checking DCC\n
set.hostname
AddressedEnvelope<ByteBuffer>
udid errorDescription 
[%s] EL @ end of Collect: %d\n
fn._read_special_reg.ibreakenable
Unknown message response bits 
 message, expected 
testChassisFan(fan:pwmToRPM:)
{%s:%s@%d} [%s] \tFailure: only %u of %u individual read transfers were done (%s)\n\n
Specified host %s did not resolve to valid host
AuthDebugWithTimer_t::need_to_authenticate_probe super returned true (need)\n
{%s:%s@%d} [%s] Cannot initialize flash for programming: %s\n
ASTRIS_ERR_SLEEPING
vlanTag()
Unexpected signal subscriber notification 
_update_register32
esr_el3
Portal Status, Changing STATUS and CMD/STAT to reflect
PROBED_SLEEPING
Failed to convert primateLoc %s to unsigned long long
pnav_filter_out_kis_stm
chip == NULL
AuthBase_t::init failed (AuthDebug_t)
fn._ocd_exec_instr.wsr.reg_srn.t1
astris_soc_release
FilePath.Component must be created from exactly one non-root component
 from ConnectX firmware image.
Corrupted reply.
chassisTriageError
read_page_descriptor
WFI
bool
No connection attempt description
{%s:%s@%d} [%s] unable to read response payload\n
SCAN
callStructMethod(selector:inputStruct:inputStructCount:outputStruct:outputStructCount:)
firmwareUpdateReady
JsonLogger: Wrote %zu bytes to '%s'
rt13/13/pgood/0v855
axi-regs
Register file 22
?
Stringify
{%s->%s} [is_64] exec: DCPSX_BASE_ENC (target_el=%d)\n
Start Address=0x%08llX....End Address=0x%08llX
{%s:%s@%d} [%s] reading PAR[64]\n
ret.modify.edscr.~ma
virtual int CPU_t::resume(bool)
fn._ocd_exec_instr.wsr.ddr.t1
.otherReadExecute
rt13/1/pgood/0v855
wrstn-partition-number
{%s:%s@%d} [%s] Writing KEY2 During Unlock Sequence Failed: %s\n\n
CPU.ARM32
Cause of last exception
Too many address breakpoint regs (%u). Maximum is 2.
fn._write_mem.bp_info
[AstrisAsync][COMPARE] acmd1->cmdbuf:\n
SRST
backtrace
ARMV6M
ret.exec.drps
Aligned Address: %llx
CPU Monitor[%i]: %s\n
Data break 0 control
RT13Updater/B2PClientChannelHandler.swift
KIS Writevals putting back the value
Transaction
com.apple.Manta.MantaLocalDataBaseFirmwareProvider
Hang Address: 0x%016llx\n
removeService(service:)
MantaAsyncXPCModule/Never.swift
{%s:%s@%d} [%s] Couldn't get CPU from AP\n
remote probe closed connection
Management network interface
INFO
param.num_data_bp_regs.invalid.2
{%s:%s@%d} [%s] switching register set\n
Update RT13 begin: 
_ACCVerifyServiceTicket
recvmsg(descriptor:msgHdr:flags:)
Setting up VLAN '
Received output 
result.read_vals(version)==
{%s:%s@%d} [%s] writing PAR[64]\n
ret.a64cpu_raise_el_hw_safe
{%s=>%s} null reference to CPU_t object, `cpu->state`
EXPLORE_LOST
MAC16 Data register 3
Failed to get panic report: 
GPR_1
AXcpu_clean_dcache
astris_command_base
fn._read_special_reg.dbreakc0
{%s} match any probe [localhost]
AXchip_fromreset
astris_convert_addr_to_die
ret._a64cpu_read_sysreg_hw.hcr_el2
FAR_EL1
~INTDIS
_invalidate_icache_vaddr
```
