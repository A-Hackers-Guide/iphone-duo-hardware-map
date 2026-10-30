# `/System/Library/PrivateFrameworks/APFoundation.framework/APFoundation`

iOS 27.2 dyld shared cache image, version `557.2.14.0.0`. Light page: libraries and type names only. **[DSC]**

## Linked libraries (29)

- `/System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport`
- `/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration`
- `/System/Library/Frameworks/Security.framework/Security`
- `/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag`
- `/System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices`
- `/usr/lib/libMobileGestalt.dylib`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/System/Library/Frameworks/CoreLocation.framework/CoreLocation`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CryptoKit.framework/CryptoKit`
- `/System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials`
- `/System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks`
- `/System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter`
- `/usr/lib/libsqlite3.dylib`
- `/usr/lib/libz.1.dylib`
- `/usr/lib/swift/libswiftCore.dylib`
- `/usr/lib/swift/libswiftCoreFoundation.dylib`
- `/usr/lib/swift/libswiftCoreLocation.dylib`
- `/usr/lib/swift/libswiftDispatch.dylib`
- `/usr/lib/swift/libswiftObjectiveC.dylib`
- `/usr/lib/swift/libswiftSynchronization.dylib`
- `/usr/lib/swift/libswiftXPC.dylib`
- `/usr/lib/swift/libswift_Builtin_float.dylib`
- `/usr/lib/swift/libswift_Concurrency.dylib`
- `/usr/lib/swift/libswift_StringProcessing.dylib`
- `/usr/lib/swift/libswiftos.dylib`

## Objective-C: 139 classes, 35 protocols (method count not recorded on light pages)

### Classes

`APAnalytics`, `APBackoffTimer`, `APClientInfo`, `APDatabaseColumn`, `APDatabaseCursor`, `APDatabaseFileUtilities`, `APDatabaseManager`, `APDatabaseMigration`, `APDatabasePath`, `APDatabaseQueryInfo`, `APDatabaseRow`, `APDatabaseTable`, `APDatabaseTelemetry`, `APDatabaseTimingLock`, `APDeviceLockedTask`, `APDiagnosticReporter`, `APDiagnosticThrottle`, `APFPDIWrapper`, `APFPDIWrapperStub`, `APFixedHTTPSessionManager`, `APFlexibleHTTPSessionManager`, `APHTTPRequest`, `APHTTPResponse`, `APHTTPSession`, `APInMemoryTTLCache`, `APJSONArchiver`, `APKeychainAnalytics`, `APKeychainServices`, `APKeychainSettings`, `APLocationInfo`, `APLocationManager`, `APMetric`, `APMetricDaemonDelivery`, `APMetricNotificationRegistrar`, `APNetworkClient`, `APNetworkClientConfig`, `APOrderedMutableDictionary`, `APPromise`, `APPurgeableCacheEntry`, `APRequirements`, `APSafeFileURL`, `APServiceItem`, `APSettings`, `APSettingsStorageCloud`, `APSettingsStorageFile`, `APSettingsStorageKeychain`, `APSettingsStorageServer`, `APSettingsStorageUserDefaults`, `APSettingsStorageVolatile`, `APSigningAuthority`, `APSigningAuthorityPoolManager`, `APSigningAuthorityPoolManagerWrapper`, `APSigningAuthoritySettings`, `APSigningClientValidator`, `APSigningContextStorage`, `APSigningRequest`, `APSigningServerRequestor`, `APSigningServerRequestorStub`, `APStorageFile`, `APStorageManager`, `APSupportedSecureEncodedClass`, `APSystemClock`, `APSystemInfo`, `APSystemInternal`, `APTestingRig`, `APUnfairLock`, `APUnfairRecursiveLock`, `APXPCActionRequester`, `APXPCActivity`, `APXPCActivityCriteria`, `APXPCConnection`, `APXPCListenerManager`, `APXPCRemoteConnection`, `MGStringQuestion`, `MetricsModuleCommon`, `NSArray`, `NSBundle`, `NSData`, `NSDate`, `NSDateFormatter`, `NSDictionary`, `NSError`, `NSISO8601DateFormatter`, `NSNull`, `NSNumber`, `NSProcessInfo`, `NSSet`, `NSString`, `NSURL`, `NSURLSessionConfiguration`, `NSUUID`, `SecRandomCopyBytesHelper`, `SystemInfoInternal`, `_TtC12APFoundation10UnfairLock`, `_TtC12APFoundation12TracingClock`, `_TtC12APFoundation13APFileManager`, `_TtC12APFoundation13WorkDataStore`, `_TtC12APFoundation15APPromiseBridge`, `_TtC12APFoundation15DatabaseManager`, `_TtC12APFoundation15WorkCoordinator`, `_TtC12APFoundation16SignpostProvider`, `_TtC12APFoundation16WorkOrderBuilder`, `_TtC12APFoundation17ActionStoreRecord`, `_TtC12APFoundation17MockingjayContext`, `_TtC12APFoundation17NullKeyValueStore`, `_TtC12APFoundation18JSONKeyValueSource`, `_TtC12APFoundation18NullKeyValueSource`, `_TtC12APFoundation20DefaultWorkerFactory`, `_TtC12APFoundation20FakeSigningAuthority`, `_TtC12APFoundation20SwiftKeychainService`, `_TtC12APFoundation20WorkCommandProcessor`, `_TtC12APFoundation21DecoratedOSSignposter`, `_TtC12APFoundation21EntitlementValidation`, `_TtC12APFoundation21TracingKeyValueSource`, `_TtC12APFoundation22CurrentTerritorySource`, `_TtC12APFoundation22DatabaseCursorInternal`, `_TtC12APFoundation22TracingLocationManager`, `_TtC12APFoundation22WorkOrderDatabaseStore`, `_TtC12APFoundation23BackgroundTaskScheduler`, `_TtC12APFoundation24SinglyCallableCompletion`, `_TtC12APFoundation25UserDefaultsKeyValueStore`, `_TtC12APFoundation26DeviceExecutionEnvironment`, `_TtC12APFoundation26PrimitiveCountryCodeSource`, `_TtC12APFoundation27RandomCohortCandidateSource`, `_TtC12APFoundation27StoredCohortCandidateSource`, `_TtC12APFoundation27SystemRandomDoubleGenerator`, `_TtC12APFoundation28CohortCandidateKeyValueStore`, `_TtC12APFoundation28TracingRandomDoubleGenerator`, `_TtC12APFoundation29ConfigurableIntBucketStrategy`, `_TtC12APFoundation29OverrideRandomDoubleGenerator`, `_TtC12APFoundation30MemoizingCohortCandidateSource`, `_TtC12APFoundation31InvalidatableSigningPoolManager`, `_TtC12APFoundation31JSONIntBucketConfigurationStore`, `_TtC12APFoundation32CachingPurposeConfigurationStore`, `_TtC12APFoundation32DefaultPurposeConfigurationStore`, `_TtC12APFoundation34KeyValueOverrideRandomDoubleSource`, `_TtC12APFoundation37PrimitiveCountrySubdivisionCodeSource`, `_TtC12APFoundation9TaskTimer`, `_TtC12APFoundation9WorkTimer`

### Protocols

`APClock`, `APDataStorable`, `APDatabasePathProvider`, `APDatabaseQueryLocking`, `APDatabaseRowProtocol`, `APDatabaseTableProtocol`, `APFPDIWrapping`, `APHTTPSessionManagerProtocol`, `APLocationManaging`, `APMetricDaemonDeliverer`, `APMetricNotificationRegister`, `APMetricNotificationRegisterOwner`, `APMetricProtocol`, `APMetricReceiving`, `APObjectStorable`, `APPurgeableCacheNotifierP`, `APSettingsProtocol`, `APSettingsStorableProtocol`, `APSigning`, `APSigningAuthorityPoolManagement`, `APSigningAuthorizable`, `APSigningServerRequesting`, `APSystemInfoProviding`, `APTelemetry`, `APXPCActionReceiver`, `APXPCActionRequesterProtocol`, `APXPCListenerDelegate`, `CLLocationManagerDelegate`, `NSCoding`, `NSCopying`, `NSLocking`, `NSObject`, `NSSecureCoding`, `NSXPCListenerDelegate`, `OS_os_transaction`

