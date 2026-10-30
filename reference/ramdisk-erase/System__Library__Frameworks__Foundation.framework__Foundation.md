# `/System/Library/Frameworks/Foundation.framework/Foundation`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 43,433,328 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 51 (Size: 8856)
Flags         = NoUndefs, DyldLink, TwoLevel, AppExtensionSafe
```

## Linked libraries (33)

- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0, reexport)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8, reexport)`
- `/System/Library/PrivateFrameworks/NSPredicateSecurityPolicy.framework/NSPredicateSecurityPolicy (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/PrivateFrameworks/CoreAutoLayout.framework/CoreAutoLayout (compatibility version 1.0.0, current version 35.0.0, weak)`
- `/usr/lib/libcmark-gfm.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libcompression.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CFNetwork.framework/CFNetwork (compatibility version 1.0.0, current version 3896.200.61)`
- `/usr/lib/libarchive.2.dylib (compatibility version 9.0.0, current version 9.2.0)`
- `/usr/lib/libicucore.A.dylib (compatibility version 1.0.0, current version 78.1.0)`
- `/usr/lib/libxml2.2.dylib (compatibility version 10.0.0, current version 10.9.0)`
- `/usr/lib/liblangid.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/Combine.framework/Combine (compatibility version 1.0.0, current version 3023.0.0)`
- `/System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal (compatibility version 5027.1.6, current version 5027.1.6)`
- `/System/Library/PrivateFrameworks/ReflectionInternal.framework/ReflectionInternal (compatibility version 5027.1.6, current version 5027.1.6)`
- `/System/Library/PrivateFrameworks/RuntimeInternal.framework/RuntimeInternal (compatibility version 5027.1.6, current version 5027.1.6)`
- `/System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking (compatibility version 1.0.0, current version 72.0.0)`
- `/usr/lib/swift/libswiftCore.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftCoreFoundation.dylib (compatibility version 1.0.0, current version 120.100.0)`
- `/usr/lib/swift/libswiftDarwin.dylib (compatibility version 1.0.0, current version 428.40.1)`
- `/usr/lib/swift/libswiftDispatch.dylib (compatibility version 1.0.0, current version 1605.40.4)`
- `/usr/lib/swift/libswiftObjectiveC.dylib (compatibility version 1.0.0, current version 973.1.0)`
- `/usr/lib/swift/libswiftObservation.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftSynchronization.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftSystem.dylib (compatibility version 1.0.0, current version 5027.0.67)`
- `/usr/lib/swift/libswiftXPC.dylib (compatibility version 1.0.0, current version 167.0.2)`
- `/usr/lib/swift/libswift_Builtin_float.dylib (compatibility version 0.0.0, current version 0.0.0, weak)`
- `/usr/lib/swift/libswift_Concurrency.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswift_DarwinFoundation1.dylib (compatibility version 1.0.0, current version 428.40.1)`
- `/usr/lib/swift/libswift_StringProcessing.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftos.dylib (compatibility version 1.0.0, current version 1090.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (772 classes, 50 protocols)

Classes: `NSAKDeserializer`, `NSAKDeserializerStream`, `NSAKSerializer`, `NSAKSerializerStream`, `NSAddressCheckingResult`, `NSAffineTransform`, `NSAggregateExpression`, `NSAllDescendantPathsEnumerator`, `NSAnyKeyExpression`, `NSArchiver`, `NSArray`, `NSArrayChange`, `NSArrayChanges`, `NSAssertionHandler`, `NSAttributedString`, `NSAttributedStringMarkdownParsingOptions`, `NSAttributedStringMarkdownSourcePosition`, `NSAutoContentAccessingProxy`, `NSAutoLocale`, `NSAutoreleasePool`, `NSBackgroundActivityScheduler`, `NSBetweenPredicateOperator`, `NSBigMutableString`, `NSBlockExpression`, `NSBlockObservationSink`, `NSBlockOperation`, `NSBlockPredicate`, `NSBoundKeyPath`, `NSBoundedByPredicateOperator`, `NSBundle`, `NSBundleResourceRequest`, `NSByteCountFormatter`, `NSCFAttributedString`, `NSCFCharacterSet`, `NSCFError`, `NSCFInputStream`, `NSCFOutputStream`, `NSCFStreamWeakDelegateWrapper`, `NSCFTimer`, `NSCFType`, `NSCache`, `NSCalendar`, `NSCalendarDate`, `NSCharacterSet`, `NSCheapMutableString`, `NSClassicHashTable`, `NSClassicMapTable`, `NSCoder`, `NSComparisonPredicate`, `NSComparisonPredicateOperator`, `NSCompletionCheckingResult`, `NSComplexOrthography`, `NSComplexRegularExpressionCheckingResult`, `NSCompoundPredicate`, `NSCompoundPredicateOperator`, `NSConcreteArrayChange`, `NSConcreteArrayChanges`, `NSConcreteAttributedString`, `NSConcreteData`, `NSConcreteFileHandle`, `NSConcreteHashTable`, `NSConcreteMapTable`, `NSConcreteMapTableValueEnumerator`, `NSConcreteMutableAttributedString`, `NSConcreteMutableData`, `NSConcreteNotification`, `NSConcreteObservationBuffer`, `NSConcreteOrderedSetChange`, `NSConcreteOrderedSetChanges`, `NSConcretePipe`, `NSConcretePointerArray`, `NSConcretePointerFunctions`, `NSConcreteProtocolChecker`, `NSConcreteScanner`, `NSConcreteSetChange`, `NSConcreteSetChanges`, `NSConcreteTask`, `NSConcreteValue`, `NSCondition`, `NSConditionLock`, `NSConstantDoubleNumber`, `NSConstantFloatNumber`, `NSConstantIntegerNumber`, `NSConstantString`, `NSConstantValueExpression`, `NSCorrectionCheckingResult`, `NSCountedSet`, `NSCustomPredicateOperator`, `NSDashCheckingResult`, `NSData`, `NSDataDetector`, `NSDate`, `NSDateCheckingResult`, `NSDateComponents`, `NSDateComponentsFormatter`, `NSDateFormatter`, `NSDateInterval`, `NSDateIntervalFormatter`, `NSDebugString`, `NSDecimalNumber`, `NSDecimalNumberHandler`, `NSDecimalNumberPlaceholder`, `NSDictionary`, `NSDimension`, `NSDirInfo`, `NSDirInfoDeserializer`, `NSDirInfoSerializer`, `NSDirectoryEnumerator`, `NSDistributedNotificationCenter`, `NSDocInfo`, `NSDocumentDeserializer`, `NSDocumentSerializer`, `NSEmojiCheckingResult`, `NSEncodingDetectionBuffer`, `NSEncodingDetectionPlaceholder`, `NSEncodingDetector`, `NSEnergyFormatter`, `NSEqualityPredicateOperator`, `NSError`, `NSException`, `NSExpression`, `NSExtendedRegularExpressionCheckingResult`, `NSExtension`, `NSExtensionContext`, `NSExtensionItem`, `NSExtensionService_Subsystem`, `NSExtensionURLResult`, `NSFalsePredicate`, `NSFileAccessArbiter`, `NSFileAccessArbiterProxy`, `NSFileAccessClaim`, `NSFileAccessIntent`, `NSFileAccessNode`, `NSFileAccessProcessManager`, `NSFileAccessProcessMonitor`, `NSFileAccessSubarbiter`, `NSFileAttributes`, `NSFileCoordinator`, `NSFileCoordinatorAccessorBlockCompletion`, `NSFileCoordinatorReacquisitionBlockCompletion`, `NSFileHandle`, `NSFileManager`, `NSFileMultipleAccessClaim`, `NSFilePresenterAsynchronousOperation`, `NSFilePresenterManagedProxy`, `NSFilePresenterOperationRecord`, `NSFilePresenterProxy`, `NSFilePresenterRelinquishment`, `NSFilePresenterXPCMessenger`, `NSFilePromiseWriteToken`, `NSFileProviderKernelFileMaterializationInfo`, `NSFileProviderKernelMaterializationInfo`, `NSFileProviderKernelPartialFolderMaterializationInfo`, `NSFileProviderMessageInterface`, `NSFileProviderMessenger`, `NSFileProviderMovingInfo`, `NSFileProviderMovingResponse`, `NSFileProviderPresenterInfo`, `NSFileProviderProxy`, `NSFileProviderService`, `NSFileProviderXPCMessenger`, `NSFileProvidingInfo`, `NSFileProvidingResponse`, `NSFileReactorProxy`, `NSFileReadingClaim`, `NSFileReadingWritingClaim`, `NSFileSubarbitrationClaim`, `NSFileVersion`, `NSFileWatcher`, `NSFileWatcherObservations`, `NSFileWrapper`, `NSFileWritingClaim`, `NSFileWritingWritingClaim`, `NSFilterObservationTransformer`, `NSFormatter`, `NSFunctionExpression`, `NSGrammarCheckingResult`, `NSHTTPCookie`, `NSHashTable`, `NSISO8601DateFormatter`, `NSInPredicateOperator`, `NSIndexPath`, `NSIndexSet`, `NSInflectionRule`, `NSInflectionRuleExplicit`, `NSInputStream`, `NSInvocation`, `NSInvocationOperation`, `NSItemProvider`, `NSItemProviderRepresentation`, `NSItemRepresentationLoadResult`, `NSJSONSerialization`, `NSKeyPathExpression`, `NSKeyPathSpecifierExpression`, `NSKeyValueAccessor`, `NSKeyValueArray`, `NSKeyValueChangeDictionary`, `NSKeyValueCollectionGetter`, `NSKeyValueComputedProperty`, `NSKeyValueContainerClass`, `NSKeyValueFastMutableArray`, `NSKeyValueFastMutableArray1`, `NSKeyValueFastMutableArray2`, `NSKeyValueFastMutableCollection1Getter`, `NSKeyValueFastMutableCollection2Getter`, `NSKeyValueFastMutableOrderedSet`, `NSKeyValueFastMutableOrderedSet1`, `NSKeyValueFastMutableOrderedSet2`, `NSKeyValueFastMutableSet`, `NSKeyValueFastMutableSet1`, `NSKeyValueFastMutableSet2`, `NSKeyValueGetter`, `NSKeyValueIvarGetter`, `NSKeyValueIvarMutableArray`, `NSKeyValueIvarMutableCollectionGetter`, `NSKeyValueIvarMutableOrderedSet`, `NSKeyValueIvarMutableSet`, `NSKeyValueIvarSetter`, `NSKeyValueMethodGetter`, `NSKeyValueMethodSetter`, `NSKeyValueMutableArray`, `NSKeyValueMutableOrderedSet`, `NSKeyValueMutableSet`, `NSKeyValueMutatingArrayMethodSet`, `NSKeyValueMutatingCollectionMethodSet`, `NSKeyValueMutatingOrderedSetMethodSet`, `NSKeyValueMutatingSetMethodSet`, `NSKeyValueNestedProperty`, `NSKeyValueNilOrderedSetEnumerator`, `NSKeyValueNilSetEnumerator`, `NSKeyValueNonmutatingArrayMethodSet`, `NSKeyValueNonmutatingCollectionMethodSet`, `NSKeyValueNonmutatingOrderedSetMethodSet`, `NSKeyValueNonmutatingSetMethodSet`, `NSKeyValueNotifyingMutableArray`, `NSKeyValueNotifyingMutableCollectionGetter`, `NSKeyValueNotifyingMutableOrderedSet`, `NSKeyValueNotifyingMutableSet`, `NSKeyValueObservance`, `NSKeyValueObservationInfo`, `NSKeyValueOrderedSet`, `NSKeyValueProperty`, `NSKeyValueProxyGetter`, `NSKeyValueProxyShareKey`, `NSKeyValueSet`, `NSKeyValueSetter`, `NSKeyValueShareableObservanceKey`, `NSKeyValueShareableObservationInfoKey`, `NSKeyValueSharedObservers`, `NSKeyValueSharedObserversSnapshot`, `NSKeyValueSlowGetter`, `NSKeyValueSlowMutableArray`, `NSKeyValueSlowMutableCollectionGetter`, `NSKeyValueSlowMutableOrderedSet`, `NSKeyValueSlowMutableSet`, `NSKeyValueSlowSetter`, `NSKeyValueUndefinedGetter`, `NSKeyValueUndefinedSetter`, `NSKeyValueUnnestedProperty`, `NSKeyedArchiver`, `NSKeyedUnarchiver`, `NSLengthFormatter`, `NSLikePredicateOperator`, `NSLinguisticTagger`, `NSLinkCheckingResult`, `NSListFormatter`, `NSLocale`, `NSLocalizableString`, `NSLocalizedNumberFormatRule`, `NSLock`, `NSLookupMatch`, `NSMachBootstrapServer`, `NSMachPort`, `NSMapObservationTransformer`, `NSMapTable`, `NSMassFormatter`, `NSMatchingPredicateOperator`, `NSMeasurement`, `NSMeasurementFormatter`, `NSMessagePort`, `NSMessagePortNameServer`, `NSMetadataItem`, `NSMetadataQuery`, `NSMetadataQueryAttributeValueTuple`, `NSMetadataQueryResultGroup`, `NSMethodSignature`, `NSMorphology`, `NSMorphologyCustomPronoun`, `NSMorphologyPronoun`, `NSMultiReadUniWriteLock`, `NSMutableArray`, `NSMutableAttributedString`, `NSMutableCharacterSet`, `NSMutableData`, `NSMutableDictionary`, `NSMutableIndexSet`, `NSMutableOrderedSet`, `NSMutableRLEArray`, `NSMutableSet`, `NSMutableString`, `NSMutableStringProxyForMutableAttributedString`, `NSNotification`, `NSNotificationCenter`, `NSNotificationObservable`, `NSNotificationQueue`, `NSNull`, `NSNullFileHandle`, `NSNumber`, `NSNumberFormatter`, `NSObject`, `NSObservableKeyPath`, `NSObservation`, `NSObservationBuffer`, `NSObservationSink`, `NSObservationSource`, `NSObservationTransformer`, `NSObservedValue`, `NSObserverKeyPath`, `NSOldValueObservationTransformer`, `NSOperation`, `NSOperationQueue`, `NSOrderedCollectionChange`, `NSOrderedCollectionDifference`, `NSOrderedSet`, `NSOrderedSetChange`, `NSOrderedSetChanges`, `NSOrthography`, `NSOrthographyCheckingResult`, `NSOutputStream`, `NSOwnedDictionaryProxy`, `NSPageData`, `NSPathStore2`, `NSPersonNameComponents`, `NSPersonNameComponentsFormatter`, `NSPhoneNumberCheckingResult`, `NSPinyinString`, `NSPipe`, `NSPlaceholderMutableString`, `NSPlaceholderNumber`, `NSPlaceholderString`, `NSPlaceholderValue`, `NSPointerArray`, `NSPointerFunctions`, `NSPort`, `NSPortMessage`, `NSPortNameServer`, `NSPredicate`, `NSPredicateOperator`, `NSPredicateValidator`, `NSPresentationIntent`, `NSProcessInfo`, `NSProgress`, `NSProgressPublisherProxy`, `NSProgressRegistrar`, `NSProgressSubscriberProxy`, `NSProgressValues`, `NSPropertyListSerialization`, `NSProtocolChecker`, `NSProxy`, `NSPurgeableData`, `NSQuoteCheckingResult`, `NSRLEArray`, `NSRTFD`, `NSRecursiveLock`, `NSReduceObservationTransformer`, `NSRegularExpression`, `NSRegularExpressionCheckingResult`, `NSRelativeDateTimeFormatter`, `NSReplacementCheckingResult`, `NSRunLoop`, `NSScanner`, `NSSecureUnarchiveFromDataTransformer`, `NSSecurityScopedURLWrapper`, `NSSelfExpression`, `NSSet`, `NSSetChange`, `NSSetChanges`, `NSSetExpression`, `NSSimpleAttributeDictionary`, `NSSimpleAttributeDictionaryEnumerator`, `NSSimpleCString`, `NSSimpleOrthography`, `NSSimpleRegularExpressionCheckingResult`, `NSSmartPunctuationController`, `NSSmartQuoteOptions`, `NSSortDescriptor`, `NSSpellCheckingResult`, `NSStackObservedValue`, `NSStream`, `NSString`, `NSStringPredicateOperator`, `NSSubqueryExpression`, `NSSubrangeData`, `NSSubstitutionCheckingResult`, `NSSubstringPredicateOperator`, `NSSymbolicExpression`, `NSTask`, `NSTermOfAddress`, `NSTernaryExpression`, `NSTextCheckingKeyEvent`, `NSTextCheckingResult`, `NSThread`, `NSTimeZone`, `NSTimer`, `NSTokenMatchingPredicateOperator`, `NSTransitInformationCheckingResult`, `NSTruePredicate`, `NSURL`, `NSURLComponents`, `NSURLDirectoryEnumerator`, `NSURLError`, `NSURLFileTypeMappings`, `NSURLHostNameAddressInfo`, `NSURLKeyValuePair`, `NSURLPromisePair`, `NSURLQueryItem`, `NSURLQueue`, `NSURLQueueNode`, `NSUTIPredicateOperator`, `NSUUID`, `NSUbiquitousKeyValueStore`, `NSUnarchiver`, `NSUndoManager`, `NSUndoManagerProxy`, `NSUnit`, `NSUnitAcceleration`, `NSUnitAngle`, `NSUnitArea`, `NSUnitConcentrationMass`, `NSUnitConverter`, `NSUnitConverterLinear`, `NSUnitConverterReciprocal`, `NSUnitDispersion`, `NSUnitDuration`, `NSUnitElectricCharge`, `NSUnitElectricCurrent`, `NSUnitElectricPotentialDifference`, `NSUnitElectricResistance`, `NSUnitEnergy`, `NSUnitFormatter`, `NSUnitFrequency`, `NSUnitFuelEfficiency`, `NSUnitIlluminance`, `NSUnitInformationStorage`, `NSUnitLength`, `NSUnitMass`, `NSUnitPower`, `NSUnitPressure`, `NSUnitSpeed`, `NSUnitTemperature`, `NSUnitVolume`, `NSUserActivity`, `NSUserDefaults`, `NSValue`, `NSValueTransformer`, `NSVariableAssignmentExpression`, `NSVariableExpression`, `NSWeakObjectValue`, `NSXMLParser`, `NSXPCCoder`, `NSXPCConnection`, `NSXPCDecoder`, `NSXPCEncoder`, `NSXPCInterface`, `NSXPCListener`, `NSXPCListenerEndpoint`, `UIKit_PKSubsystem`, `_NSActivityAssertion`, `_NSAssumedFallbackInflectionAttributeDescriptor`, `_NSAttributeDescriptor`, `_NSAttributedStringFromMarkdownCreatorConcrete`, `_NSAttributedStringGrammar`, `_NSAttributedStringGrammarInflection`, `_NSAttributedStringReplacement`, `_NSAutoCalendar`, `_NSAuxiliaryUndoManagerReference`, `_NSBPlistMappedData`, `_NSBPlistMappedString`, `_NSBarrierOperation`, `_NSBundleBridge`, `_NSBundleDidLoadNotificationPayloadArray`, `_NSBundleInfoDictionary`, `_NSBundleODRDataCommon`, `_NSBundleODRDataForApplications`, `_NSBundleODRDataForExtensions`, `_NSBundleODRTag`, `_NSBundleOnDemandResourceClientExportedObject`, `_NSCalendarBridge`, `_NSCallStackArray`, `_NSClStr`, `_NSCloudSharingDescriptor`, `_NSClrDat`, `_NSClrDatM`, `_NSConcreteBlockSinkObservation`, `_NSConcreteDateInterval`, `_NSConcreteObservation`, `_NSConstantIndexSet`, `_NSDataCompressor`, `_NSDispatchData`, `_NSExtensionContextVendor`, `_NSFCUncancellableBlockOperation`, `_NSFileAccessAsynchronousProcessAssertion`, `_NSFileAccessAsynchronousProcessAssertionScheduler`, `_NSFileAccessClaimPresenterRelinquishment`, `_NSFileManagerBridge`, `_NSFileWatcherDirectoryFileHandleInfo`, `_NSFileWatcherFileHandleInfo`, `_NSIPCallbackSerialization`, `_NSImmortalCharacterSetBridge`, `_NSIndexSetEnumerator`, `_NSInflectionAttributeDescriptor`, `_NSInflectionRuleAutomatic`, `_NSInflectionRuleExplicit`, `_NSInlineData`, `_NSInlineObserverList`, `_NSIsNilTransformer`, `_NSIsNotNilTransformer`, `_NSItemProviderTypeCoercion`, `_NSJSONReader`, `_NSJSONRoundTrippingNumber`, `_NSJSONWriter`, `_NSKVO1Adaptor`, `_NSKVOCompatibility`, `_NSKVODeallocSentinel`, `_NSKeyValueDebugging`, `_NSKeyValueDebuggingDeallocSentinel`, `_NSKeyValueDidWillStats`, `_NSKeyValueObjectAndKeyPair`, `_NSKeyValueObjectBox`, `_NSKeyValueObservation`, `_NSKeyValueReturnedValueConsistencyStats`, `_NSKeyedCoderOldStyleArray`, `_NSKeyedUnarchiveFromDataTransformer`, `_NSKeyedUnarchiverHelper`, `_NSLexiconMorphunDictionary`, `_NSLocalNotificationCenter`, `_NSLocaleBridge`, `_NSLocalizedNumberFormatRuleAutomatic`, `_NSLocalizedStringResource`, `_NSLocalizedStringResourceSwiftWrapper`, `_NSMainThread`, `_NSMappingObservation`, `_NSMarkdownStringAttributeDescriptor`, `_NSMetadataItemPrivateIvars`, `_NSMetadataQueryPrivateIvars`, `_NSMetadataQueryResultArray`, `_NSMetadataQueryResultGroupArray`, `_NSMetadataQuerySortingPseudoItem`, `_NSMorphologyAttributeDescriptor`, `_NSMutableCharacterSetBridge`, `_NSNegateBooleanTransformer`, `_NSNestedDictionary`, `_NSNumberFormattingAttributeDescriptor`, `_NSNumericAttributeDescriptor`, `_NSObservableKVO1Adaptor`, `_NSObservableKeyPathChangeAdaptor`, `_NSObservableObservation`, `_NSObserverList`, `_NSObservingBlockSinkObservation`, `_NSObservingObservation`, `_NSOperationQueueProgress`, `_NSOrderedCollectionDifferenceMoves`, `_NSOwningMappingObservation`, `_NSOwningObservingObservation`, `_NSPerformanceMeter`, `_NSPersonNameComponentsData`, `_NSPersonNameComponentsFormatterData`, `_NSPersonNameComponentsStyleFormatter`, `_NSPersonNameComponentsStyleFormatterAbbreviated`, `_NSPersonNameComponentsStyleFormatterAvatar`, `_NSPersonNameComponentsStyleFormatterFamilyInitialVariant`, `_NSPersonNameComponentsStyleFormatterFamilyOnlyVariant`, `_NSPersonNameComponentsStyleFormatterGivenInitialVariant`, `_NSPersonNameComponentsStyleFormatterGivenOnlyVariant`, `_NSPersonNameComponentsStyleFormatterLong`, `_NSPersonNameComponentsStyleFormatterMedium`, `_NSPersonNameComponentsStyleFormatterNicknameVariant`, `_NSPersonNameComponentsStyleFormatterShort`, `_NSPersonNameComponentsStyleFormatterShortNameSimpleFallback`, `_NSPersonNameComponentsStyleFormatterShortVariantGeneral`, `_NSPlaceholderCharacterSet`, `_NSPlaceholderData`, `_NSPlaceholderIndexSet`, `_NSPlaceholderObservation`, `_NSPredicateOperatorUtilities`, `_NSPredicateUtilities`, `_NSProgressProxy`, `_NSProgressSubscriber`, `_NSProgressWithRemoteParent`, `_NSSharedKeySetS`, `_NSSharedValueTransformer`, `_NSStatic_NSDecimalNumber`, `_NSStatic_NSStaticUnitConverterLinear_NoConst`, `_NSStatic_NSUnitAcceleration`, `_NSStatic_NSUnitAngle`, `_NSStatic_NSUnitArea`, `_NSStatic_NSUnitConcentrationMass`, `_NSStatic_NSUnitConverterLinear`, `_NSStatic_NSUnitDispersion`, `_NSStatic_NSUnitDuration`

Protocols: `FPFileProviderRequestProxyCreating`, `NSCoding`, `NSCopying`, `NSDecimalNumberBehaviors`, `NSDeserializerStream`, `NSDiscardableContent`, `NSFastEnumeration`, `NSFileAccessArbiter`, `NSFileAccessArbiterXPCInterface`, `NSFileAccessClientLocalArbiterInterface`, `NSFileCoordinationDebugInfoXPCInterface`, `NSFileCoordinationRetainedAccess`, `NSFileCoordinatorUploadFilePreparing`, `NSFilePresenter`, `NSFilePresenterXPCInterface`, `NSFileProviderXPCInterface`, `NSItemProviderReading`, `NSItemProviderWriting`, `NSKeyValueProxyCaching`, `NSLocking`, `NSMutableCopying`, `NSObject`, `NSObservable`, `NSObserver`, `NSOwningObserver`, `NSPredicateVisitor`, `NSProgressPublisher`, `NSProgressRegistrar`, `NSProgressReporting`, `NSProgressSubscriber`, `NSSecureCoding`, `NSSerializerStream`, `NSURLSessionDataDelegate`, `NSURLSessionDataDelegatePrivate`, `NSURLSessionDelegate`, `NSURLSessionTaskDelegate`, `NSXPCConnectionDelegate`, `NSXPCListenerDelegate`, `NSXPCProxyCreating`, `ODRClientProtocol`, `ODRServerProtocol`, `OS_os_transaction`, `PKModularService`, `_NSAttributedStringFromMarkdownCreator`, `_NSBundleResourceRequestAppExtensionProtocol`, `_NSExtensionAuxHostingBase`, `_NSKVOCompatibilityShim`, `_NSUndoManagerAuxiliaryInterface`, `_NSUndoManagerMainInterface`, `_NSXPCTransport`

## Strings (18,365)

First 2,500 of 18,365.
```
softlink:r:path:/System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
%s options: %lx -- URL: %{private}@ -- purposeID: %{public}@ -- claimID: %{public}@
mismatched count of values and keys from remote progress KVO update
Unable to load main bundle: Unable to determine executable path
Unable to encode value for key %@ because it is of unsupported type %@
<NSItemProvider %{public}p> Load handler successfully provided NSItemProviderWriting object %@, calling out to -[%{public}@ _loadFileRepresentationOfTypeIdentifier:] to load the data representation of the object
Could not get container for signing identifier %s. Error: %s
Claim %{public}@ observed suspension of client with %d
Detected attribute change to %{private}@
Found language-specific rule for prefix / suffix pair: %@, %@
Cannot use inflection engine (Obtaining the token chain from a word): %{public}@
Failed to close file at %{private}@ because of error: %@
%{public}@ finished accommodateSubitemDeletion
<NSItemProvider %{public}p> Registering NSItemProviderWriting object of class %{public}@ with declared types %{public}@
Releasing assertion after sending message to %{public}s
Claimer for %{public}@ is waiting for presenter %{public}@ on %{public}s to relinquish
NSPredicate: Using NSExpression CAST(x,'%{public}@') is deprecated and will be removed in a future release.  '%{public}@' should not be cast into type '%{public}@' through initWithString
A server unexpectedly received a updateLastEventID: message
NSBundle %@ loading failed because an exception was raised during loading %@
NSUndoManager<%p> (aux) is sending a remote undo registration with UUID %@ to its main undo manager over connection %@
A subarbiter was told by a superarbiter about a file reconnection, which is a surprise.
NSPredicate: Using NSFunctionExpression with selector '%@' and return type '%s' is forbidden
<NSItemProvider %{public}p> Loading data representation for type identifier '%{public}@'
<NSItemProvider %{public}p> Calling -[%{public}@ objectWithItemProviderData:] failed with error: %@
This process is unable to access File Coordination's debug information due to insufficient permissions.
Presenter %{public}@ settling non-coordinated events
NSBundle %@ initWithPath failed because the resolved path is empty or nil
NSBundle %@ principal class is nil because all fallbacks have failed
Error in extension removing asset packs: %@
[NSFileAccessNode assertDead] found a surprisingly live node.
#fsevents FSEventStreamStart() returned NO. Path: %{private}@
RegisterPlugInType: No factory registered for %{public}s
Attempt to load executable of a type that cannot be dynamically loaded for %{public}s
Unpin: Bundle 0x%p / Asset Pack ID: %{public}@
Read (Async) options: %lx -- URL: %{private}@ -- purposeID: %{public}@ -- claimID: %{public}@
Claim %{public}@ is waiting for file %{private}@ to be prepared for uploading
(ReadingForUploading) Copying cordinated flat file
NSPredicate: NSFunctionExpression must return an object
No provider found for reparent request - req: %d
Received item disappearance hint with purpose %{public}@ -- %{private}@
A subarbiter is being notified of a sharing change and it's not even subarbitrating yet, which is a surprise.
Connection to filecoordinationd interrupted. Attempting to re-add presenters
A server unexpectedly received a observeChangeWithSubitemURL: message
Making presenter %{public}@ observe reconnection
Claim %{public}@ is blocked by subarbitration claim %{public}@
Bundle %{public}s contains a factory ID of %s which is not a valid UUID. Not registering.
Unable to load .stringsdict file: %s / %s: %s
NSPredicate: NSCustomPredicateOperator unable to find method
Add key: %{public}@ to entitlement cache for connection: %{public}@
NSFileCoordinator does not handle NSURLs that return relative or empty paths when sent -path, like this one:\n%{private}@
Cannot find executable for %{public}s
Static resource lookup for resources of type %{private}s %{private}s failed - not a bundle
AddInstanceForFactory: Removed instance for id %s
NSPredicate: Using NSFunctionExpression with selector '%@' and parameter encoding '%s' is forbidden
%{public}s: %{public}@
%{public}@ providing physical URL
Received reacquisition reply for presenter %{public}@ after claim %{public}@
-[NSFileAccessNode url] is returning nil.
NSBundle %@ loading failed because the file does not exist
Too many variant permutations to compute: %@
Error communicating with service named: %{public}@. %{public}@
A subarbiter is trying to forward a claim revocation to its superarbiter, but the connection is already gone, which is a surprise.
Removed provider %{public}@
Making presenter %{public}@ setLastPresentedItemIdentifier: %llu
Value for width table in stringsdict was not a string or dictionary
%{public}@ allowed unarchiving safe plist type '%{public}@' for key '%{public}@', even though it was not explicitly included in the client allowed classes set: '%{public}@'. This will be disallowed in the future.%{public}@
NSPredicate: Unarchiving an NSCustomPredicateOperator is deprecated and secure coding support will be removed in a future release.
<NSItemProvider %{public}p> Calling out to a load operator from NSItemProvider's unarchived object for type identifier '%{public}@'
Added provider %{public}@ failed because no node was found
%{public}@ finished validate subitem relinquishment with reply: %s
Resource lookup for resources of type %{private}s %{private}s failed - could not convert to file system representation
NSUndoManager<%p> (main) failed to connect to an auxiliary manager: %@
<NSItemProvider %{public}p> Registering %{public}@ representation for type '%{public}@'
<NSItemProvider %{public}p> Calling out to -[%{public}@ loadDataWithTypeIdentifier:] to provide data representation for object
<NSItemProvider %{public}p> Expected class is a URL and the type identifier is a URL, loading the object as an NSURL
Load resulted in data but a file was requested; NSItemProvider will write the data to a temporary file
Asking provider %{public}@ to provide physical URL
Cannot use inflection engine (Annotating the token chain): %{public}@
*** unum_clone() failed in NSUnitFormatter: %s, icuNF: %p
Unable to consume sandbox extension for path '%s' (errno: %{public}d)
<NSItemProvider %{public}p> Calling out to load handler to provide NSItemProviderWriting object
Claim %{public}@ can't be granted in daemon
Failed to write filecoordinationd dump file to %@. Received exception: %@\n%@
Received item disconnection hint with purpose %{public}@ -- %{private}@
A subarbiter was told by a superarbiter about a file ubiquity change, which is a surprise.
fileproviderd (%d) finished preparing providers
NSInflectionAgreementConcept attribute in range %{public}@ is set to %{public}ld which is out of bounds.
Appending path component %{private}@ (length: %lu) to string %{private}@ (length: %lu) resulted in an embedded NUL character
<NSItemProvider %{public}p> Finished loading data representation for type identifier '%{public}@' with %lu bytes of data
<NSItemProvider %{public}p> Loading data representation for type
Unblocking claimer for claim %{public}@ because the claim it was avoiding a deadlock with finished: %{public}@
A subarbiter was told by a superarbiter about a file change, which is a surprise.
A subarbiter is being notified of a change, which is a surprise.
A presented file was moved but its new name couldn't be gotten. Error: %i
<NSItemProvider %{public}p> Finished loading file representation for type identifier '%{public}@' and successfully created a temporary copy at %@
<NSItemProvider %{public}p> Loading in-place file representation for type identifier '%{public}@'
Begin: Request 0x%p was cancelled (error: %@)
Failed to copy loaded result (%@) to a temporary directory: %@
Prelinquishment requested, but already asked to relinquish. Adding a new relinquishment reply
-[NSFileVersion removeAndReturnError:]: You can't use it with a backup version.
No file watcher could be started. URL: %{private}@
Encountered read failure %d %s
NSUndoManager<%p> (aux) performing %{public}@ %{public}@ triggered from remote
<NSItemProvider %{public}p> An in-place load was requested but the file was not loaded in-place, NSItemProvider will provide a URL to a temporary copy created at %@
NSBundleResourceRequest helper daemon reports an error beginning for bundle %@: %@
*** uameasfmt_formatMultiple() failed in NSUnitFormatter: %s, len = %d
%{public}@ finished accommodateSubitemEviction
-[NSFileVersion setResolved:] tried but failed. The error is:\n%@
Resource lookup at %{private}s\n\tRequest       : %s%s\n\tResult        : %s
No ArchivingExceptions available / readable. Allowing all.
unable to create RTF representation of attributed string! error - %@
NSUndoManager<%p> (main) opening cross-process connection to auxiliary undo manager with UUID %{public}@
NSPredicate: Use of %@ with instance of '%{public}@' is forbidden.
Received item ubiquity change hint with purpose %{public}@ -- %{private}@
#filereference Detected move from %{private}@ to %{private}@
There was an error parsing the filtered Info.plist at path %{private}s: %{public}s - %{public}ld
init(path:) failed because the resolved path is not representable %{private}s
NSInflect attribute is an internal inflection object (%@), using it in range %{public}@
Added provider %{public}@ failed because -setItemLocation: failed
No provider found for materialization - req: %d
Failed to set correct permissions for filecoordinationd dump file at %@
Received item move hint with purpose %{public}@ -- %{private}@ -> %{private}@ (fileID: %llu)
Unable to resolve directory %d
User morphology preferences value read from the shared domain: %@ (is present? %{public}s)
Range %{public}@ of string with length %lld -- edited target inflection with attributes from replacements that are unambiguous nouns: %@.
Inflection engine is enabled? %{public}s for language %{public}@
Cannot use inflection engine (Obtaining dictionary names for grammemes): %{public}@
<NSItemProvider %{public}p> Requesting data of type '%{public}@'; reporting as data of type '%{public}@'
Begin: Request 0x%p response: Error: %@
NSURL parameterString is deprecated and now always returns nil. The path component now includes the part of the URL string which parameterString used to return.\nURL = %{private}@
%@: attempting to deallocate an immortal bundle - break on _NSBundleDeallocatingImmortalBundle to debug. This bundle %p has been overreleased.\n\tBundle Identifier: %@\n\tBundle URL: %@
Range %{public}@ of string with length %lld -- edited target inflection with numbers supplied as replacements with result: %@.
Class '%{public}@' unexpectedly found in possibly-altered archive. -[%{public}@ classForCoder] is inherited from a superclass and should likely have replaced this object at encode time. To be allowed in archives, it should override -classFo
<NSItemProvider %{public}p> Calling out to load handler to produce NSSecureCoding object for type identifier: '%{public}@' with expected class %{public}@
udtitvfmt_open failed!  Tried to set template: %@ for locale %s and timezone %@ and got status code: %s
Killing %d because it was suspended when we tried to send it an NSFilePresenter message
NSFileCoordinator instance %p was cancelled. All future claims made on this instance will immediately fail with cancellation
A subarbiter is being notified of cancellation and it's not even subarbitrating yet, which is a surprise.
Using ~iphone resources (classic)
NSBundle %@ principal class is using first class name %@ because the bundle's principal class name %@ is not present
NSInflectionReferentConcept attribute in range %{public}@ is set to %{public}ld which is out of bounds.
<NSItemProvider %{public}p> Loading NSSecureCoding item for type identifier: '%{public}@'
Killing process because it has oustanding messages
Could not read values in %s: accessing these preferences requires user-preference-read or file-read-data sandbox access
Read options: %lx -- URL: %{private}@ -- purposeID: %{public}@ -- claimID: %{public}@
Stopping subarbitration
<NSProgressSubscriberProxy %p> Add publisher ID %{public}@ for URL %{private}@ in category %{public}@
NSUndoManager<%p> (aux) received an in-process connection request from a main undo manager whose undo actions cannot merge cleanly with the auxiliary undo actions. The undo/redo stack will be cleared.
NSUndoManager<%p> (aux) received a cross-process connection request from a main undo manager but items are present on the redo stack. The undo/redo stack will be cleared.
NSUndoManager<%p> (aux) receiving connection request from remote main undo manager
NSFileCoordinator: A superarbiter was told to start arbitrating, which is a surprise.
Presenter %{public}@ not allowed to tie to URL -- %{private}@
Making presenter %{public}@ savePresentedItemChanges
Making presenter %{public}@ accommodateDisconnection
Cannot use inflection engine (Obtaining surface form grammemes): %{public}@
Removing temporary folder at %@ created for an in-place load of an item that provided a copy representation
Skipping path %{private}@ for %{public}@ because path it is private
Adding presenter %{public}@ for URL: %{private}@
%{public}@ providing %{private}@ for claim %{public}@
Detected move of %{private}@ to %{private}@
Starting to watch %{private}@
NSFileCoordinator: dispatch_source_create() returned NULL, which is a surprise.
%s not found in table %s of bundle %s
<NSItemProvider %{public}p> Providing nil response from no-op/non-existent load operator
No container for %{public}@, so we will not manage the connection
Failed to set thread materialization iopolicy value (%d): %{darwin.errno}d
Sending of a '%{public}@' message was interrupted: %{public}@
A server unexpectedly received a observeChangeOfUbiquityAttributes: message
<NSProgressSubscriber %p> Add publisher %p forID: %{public}@
Internal error unloading bundle %{private}s: %{public}s
NSPredicate: -[NSPredicate copy] called on a predicate that has _evaluationBlocked set. The resulting copy will drop _evaluationBlocked.
NSUndoManager<%p> (main) opening in-process connection to auxiliary undo manager with UUID %{public}@
Load did not provide a result value; error: %@
An arbiter is confusing itself after a file was moved while telling claims about node replacement
Making presenter %{public}@ accommodateSubitemEviction for %{private}@
A process invoked -[NSFileCoordinator prepareForReadingItemsAtURLs:options:writingItemsAtURLs:options:error:byAccessor:] but stopped listening. Letting other process' file access claims proceed.
valueForEntitlement couldn't load a Security symbol.
Language lookup at %{private}s\n\tLocalizations : %s\n\tDev language  : %s\n\tUser prefs    : %s\n\tMain bundle   : %s\n\tAllow mixed   : %s %s\n\tResult        : %s\n
 reason=%{signpost.telemetry:string1,public}@ version=%{signpost.telemetry:string2,public}@  enableTelemetry=YES 
 abandoned=%{signpost.telemetry:number1,public}d 
%{public}@: Exception caught during decoding of reply to message '%{public}s', dropping incoming message and calling failure block.\n\nIgnored Exception: %{public}@
NSXPCListener: received error or other non-connection type in handler for remote listener: %{public}s
Unable to load .strings file: %s / %s: %@
Inflection engine reported an error for '%s' while attempting to inflect: %@
Connection to filecoordinationd interrupted. Attempting to re-add providers
Settling watcher for %{private}@
Notifying the observer. Subitem path: %@, event kind: %p, event path: %@
dlfcn check load bundle %{private}s mode %d no handle
Fail to get skeleton from date format %@; error: %s
NSFileProviderMessenger failed to get proxy factory: %{public}@
Unexpected state upon completion of beginAccessingResourcesWithCompletionHandler (error handler) (%lld)
Unexpected state upon completion of conditionallyBeginAccessingResourcesWithCompletionHandler (unavailable case) (%lld)
%{public}@: received an undecodable message (no protocol set to define allowed messages on exported object). Dropping message.
%{public}@: received an undecodable message (invocation with no selector)
A `formatNumber` attribute is present, but no locale has been specified for formatting. The attribute will have no effect.
%{public}@: '%{public}@' is not a subclass of NSValueTransformer.
Unsupported store type: %zd
%{public}@ received an undecodable message (incompatible reply block signature for %{public}s (wire: %{public}@ vs local: %{public}@)
User morphology was cleared.
implicit decoding of plist types, like `[unarchiver decodeObjectOfClass:[NSString class] forKey:...]` allowing a decode of a `NSNumber` are no longer allowed. Please ensure you list all the expected types including core plist types like `NS
%@: Thread creation failed with error %d
NSPredicate: Using NSExpression CAST(x,'Class') is deprecated and will be removed in a future release.  '%{public}@' should not be cast into a Class object
Exception thrown while loading item with type identifier '%{public}@': %@
Failed to remove file created for uploading: %{public}@
Service %{public}@ has requested we fall back to the standard procedure to prepare file %{private}@ for uploading.
dlsym cannot find symbol %s: %{private}s
Unable to load .strings file: %s / %s: %s
%{public}@ -- Note: %{public}@.
Provider %{public}@ finished providing physical URL
<NSProgressSubscriber %p> Stop for ID %{public}@
*** Assertion failure in %@(), %@:%ld
This SPI will be removed in future releases. Please switch to using normal `NSSecureCoding` API like '-[NSKeyedUnarchiver decodeObjectOfClasses: forKey:]' instead
Load resulted in a URL (%@) that can be opened in-place and an in-place file was requested; NSItemProvider will vend the provided URL to load in-place
Letting claim %{public}@ go before blocking claim %{public}@ because the latter is blocked by another claim with the former's purposeID: %{public}@
Bundle %{public}s contains a factory ID of 00000000-0000-0000-0000-000000000000 with function 'MyFactoryFunction'. This bundle is not a valid plugin.
Unable to read all keys from .stringsdict file: %s / %s: no result
In-flight claim %{public}@ was cancelled
Subarbitration claim %{public}@ blocked pending grantAccessClaim
NSDocument called rmdir(\"%@\"), it didn't return 0, and errno was set to %{errno}d.
Using ~ipad resources (classic)
NSPredicate: Using NSCustomPredicateOperator with selector '%@' and return type '%s' is forbidden
NSUndoManager<%p> (aux) has opened an in-process connection to a main undo manager as %{public}@
A subarbiter is being notified of item reconnection, which is a surprise.
Deferring presenter %{public}@ reaquistion for .5 seconds
Invoking reacquirer because all claims were removed
Fetch error occurred: %@
Notification center message dropped due to buffer limit. Check sequence iterator frequently or increase buffer size. Message: %s
sandboxing denied subscription to progress on URL %@ (bundle id %@, %@)
Range %{public}@ of string with length %lld -- edited target inflection with attributes from replacements that could be nouns or adjectives: %@.
Decoder with secure coding enabled is decoding a cycle. See rdar://105473537 for help\n
NSUndoManager<%p> (aux) has opened a cross-process connection to a main undo manager as %{public}@
Removing temporary file %@ created for in-place load of copied file
Refused to register file watcher for file at path %{private}@ on behalf of an NSFilePresenter because the requesting process does not have access to it
This bundle %p does not have a valid path. Using backstop: %@
<NSItemProvider %{public}p> Finished loading in-place file representation for type identifier '%{public}@' with error: %@
<NSItemProvider %{public}p> Loading object of class %{public}@
Claim %{public}@ was revoked
Claim %{public}@ granted in client
Claim %{public}@ failed during preparing for uploading due to error: %@
Starting subarbitration for %lu URLs
A subarbiter was told by a superarbiter about a file disconnection, which is a surprise.
`WrappedBundle` link invalid or pointed outside bundle at %{public}s
API MISUSE: URL(filePath:) called with an HTTP URL string. Using URL(string:) instead.
Value for 'AppleLanguages' found in preferences contains no valid entries; falling back to default locale identifier as current
<NSItemProvider %{public}p> Calling out to -[%{public}@ _loadFileRepresentationOfTypeIdentifier:] to provide data representation for object
<NSItemProvider %{public}p> Loading in-place file representation for type
Re-allowing suspension for pid: %d
Write options: %lx -- URL: %{private}@ -- purposeID: %{public}@ -- claimID: %{public}@
Successfully copied loaded result (%@) to a temporary location (%@)
Revoking claim %{public}@ prior to invoking accessor
%{public}@ grantAccessClaim message failed: %{public}@
A subarbiter is being notified of file movement and it's not even subarbitrating yet, which is a surprise.
NSDocument could not create temporary version storage at %@. Here's the error:\n%@
A file watcher that has been started but not stopped is being deallocated
Notifying the observer. Subitem path: <none>, event kind: %p, event path: %{private}@
%{public}@: received an undecodable message (invocation with no signature info)
%{public}@: received an undecodable message (remote asked for no reply, but we expected one). Dropping message.
Bundle %{public}s contains a factory function which is not a string. Not registering.
KVO ISSUE -- MAY CAUSE CRASHES -- An observer was deallocated before it removed itself from its outstanding observations, while those objects remain active in memory. Observer: %{public}@, Outstanding observations: %{public}@, Deallocated a
Removing the temporary item at %@ (created for an in-place load of a file that was copied) as part of a coordinated delete
Subarbitration claim %{public}@ was nullified
Detected deletion of %{private}@
URL %{private}@ reset unnecessarily
NSPredicate: Archiving an NSCustomPredicateOperator is deprecated and secure coding support will be removed in a future release.
NSFileWrapper could not delete the temporary item at %@. Here's the error:\n%@
Telling presenter %{public}@ to reacquire after claim %{public}@
Subarbitration claim %{public}@ invoked in server
Cannot find function pointer %s for factory %s
Value for %s in width table in stringsdict was not a dictionary
 reason=%{signpost.telemetry:string1,public}@ version=%{signpost.telemetry:string2,public}@  enableTelemetry=YES  isAnimation=YES
NSUndoManager<%p> (main) undo actions cannot be merged with an auxiliary cleanly. The undo/redo stacks will be cleared.
*** uameasfmt_getUnitsForUsage() failed in NSUnitFormatter: %s
Claim %{public}@ invoked in server
Revoking claim %{public}@ because client died
Registering presenter %{public}@ disallowed. Process %d is not allowed to access the requested path or any of its parent directories: %{private}@
<NSItemProvider %{public}p> Unable to find suitable representation conforming to type identifier '%{public}@'
Scheduling suspension prevention of pid %d for activity: %{public}@
Claim %{public}@ invoked in client
NSFileCoordinator only handles URLs that use the file: scheme. This one does not:\n%{private}@
%{public}@: received an undecodable message for proxy %lld (no exported object to receive message). Dropping message.
Factory %s does not support type %s
dlfcn image path for pointer %{public}s is %{private}s
Inflection engine reported an error in mdv_create: %@
Upload preparation for claim %{public}@ completed with resulting URL: %{private}@
A subarbiter is being notified of item disappearance, which is a surprise.
Telling presenter %{public}@ to reacquire
Kernel asking provider %{public}@ to provide %{private}@
NSPredicate: Use of '%{public}@' as an NSExpression function is forbidden.
KVCFun
Error in extension adding asset packs: %@
Failed to get a GSAddition with persistent identifier: %@. Here's the error: %@
loctable overridden by installed files. Bundle: %s, table: %s
<NSItemProvider %{public}p> Successfully loaded data representation and initialized type of class %{public}@
Begin: Request (Conditional) 0x%p response: Available %lu : %d packs
Provider %{public}@ finished providing for kernel
`WrappedBundle` link too short or pointed outside bundle at %{public}s
Bundle %{public}s contains a type ID which is not a valid UUID. Not registering.
NSKeyedUnarchiver was created with secure coding implicitly disabled. This simulated crash will soon turn into an actual crash. See rdar://104622435 for help.
Encountered fstat failure %d %s
A subarbiter is being notified of a ubiquity change and it's not even subarbitrating yet, which is a surprise.
Making presenter %{public}@ setProviderPurposeIdentifier: %{public}@
Asking presenter %{public}@ to relinquish to claim %{public}@
Presenter %{public}@ has sent a %@ response, unblocking subarbitration claimer: %{public}@
Not advancing in firstInstant(of:at:). unit: %{public}s, at: %{public}f
Encountered %s failure %d %s
Cannot use inflection engine for language %{public}@ (Creating a tokenizer): %{public}@
<NSItemProvider %{public}p> Loading item of expected class %{public}@ for type identifier '%{public}@'
Provider %{public}@ has finished providing a physical URL, unblocking claimer for %{public}@
Asking service named %{public}@ to prepare file %{private}@ for uploading
A server unexpectedly received a accommodateDeletionOfSubitemAtURL: message
Making presenter %{public}@ accommodateSubitemDeletion for %{private}@
Overflowing in firstInstant(of:at:). unit: %{public}s, at: %{public}f
Range %{public}@ of string with length %lld will be inflected with requested inflection: %@, resolved inflection %@
<NSItemProvider %{public}p> Successfully loaded in-place file representation and initialized type of class %{public}@
Pin: Bundle 0x%p / Asset Pack ID: %{public}@ / URL: %{private}@
KVO ISSUE: , key: %{public}@ -- Has called 'will's but did not pair with enough 'did's during the same run loop spin
NSPredicate: %@ with selector '%{public}@' is forbidden.
%{public}@ finished accommodateDisconnection
Cancelling providing for claim %{public}@
loctable overridden by installed files. Bundle: %s, table: %s, language: %s
%@ tried to read the file wrapper's contents lazily but an error occurred: %@
Failed to open %@ for filecoordinationd dump file: %s
NSFileVersion invoked -[NSFileManager URLForDirectory:inDomain:appropriateForURL:create:error:] and that failed. Here's the error:\n%@
Manually unsettling watcher for %{private}@
<NSProgressSubscriber %p> Ignoring add publisher %p forID: %{public}@, because subscriber is stopped
Unable to read key-paths %s from .stringsdict file: %s / %s: no result
*** Application: %s just recreated special folder: %s
LocalizedStringResource did not contain a sandbox extension token. Proceeding to lookup localized string without consuming a sandbox extension.
%{public}@: value for key (%{public}@) is not an object. This will become an error in the future.
Could not convert signing identifier %{public}@
Nullified subarbitration claim %{public}@ to because of a blocking subarbitration claim: %{public}@
Invoking reacquirer, because no claims remain
dlfcn load bundle %{private}s mode %d
udtitvfmt_setAttribute failed!  Tried to set minimize type: %ld and got status code: %s
User morphology produced: %@
NSCoder couldn't load a Security symbol.
<NSItemProvider %{public}p> Loading in-place file representation for type identifier '%{public}@' finished loading (%@)
Unable to connect to daemon to get preservation priority
[NSURL setIOPolicy:] sandbox_check: current process does not allow iopolicy syscalls
*** uameasfmt_format() failed in NSUnitFormatter: %s, len = %d, value = %f, unit = %lu
Write (Subarbitration) options: %lx -- URL: %{private}@ -- purposeID: %{public}@ -- claimID: %{public}@
An exception occurred while attempting to gather debug information: %@\n%@
Unable to issue sandbox extension for path '%s' (errno: %{public}d)
NSInflectionAgreementArgument attribute in range %{public}@ is set to %{public}ld which is out of bounds.
Detected file move on behalf of writing claim %{public}@
Unsettling watcher for %{private}@ in response to event
Fail to get calendar units from date format %@; skeleton: %@
Detected process suspension: %i
[NSFileProviderProxy setItemLocation:] was invoked for a provider proxy that already has a location. Ignoring it.
There was an error parsing the Info.plist at path %{private}s: top level keys were not strings
User morphology preferences value read from the standard user defaults: %@ (is present? %{public}s)
Cannot use inflection engine (Checking that the token is the correct type): %{public}@
NSCoding is deprecated, and does not support NSSortDescriptor's reverseNullOrder property.  Please use keyed archiving instead.
*** uameasfmt_getUnitName() failed in NSUnitFormatter: %s, len = %d
*** uplrules_open() failed in NSUnitFormatter: %s
A file coordination client died
<NSProgressSubscriberProxy %p> Remove publisher ID %{public}@
<NSItemProvider %{public}p> Loading file representation for type identifier '%{public}@'
NSBundleResourceRequest encountered a sandboxing error for bundle %@: %d
Creating process monitor for pid %d
Not materializing provider-less directory - req: %d
Bundle %{public}s contains a factory ID which is not a valid UUID. Not registering.
Unable to remove observer. The provided token does not belong to this notification center. Expected: <%s 0x%s>, got <%s 0x%s>.
NSPredicate: Using NSFunctionExpression on a Class '%{public}@' is deprecated and will be removed in a future release.  NSFunctionExpression should operate on instances.
unable to create attributed string representation from RTF data! error - %@
Begin: Request 0x%p response: %lu packs now available
KVO ISSUE: %{public}@ -- MAY CAUSE CRASHES -- The value for this key pair seems to have changed outside of a will/did pair AND IT IS OBSERVED BY OTHER OBJECTS!!!; last observed value was '%{public}@', current value is '%{public}@'
A server unexpectedly received a observeReconnection message
Making presenter %{public}@ observe ubiquity change
Extensions of wrapped bundles did not match at %{public}s
Both NSInflectionAgreementArgument and NSInflectionAgreementConcept attributes specified in range %{public}@. The latter will be discarded.
Could not get signing identifier: %@
-[NSFileWrapper initWithSerializedRepresentation:] encountered an invalid preferredFileName: %{private}@
Re-evaluating claims pending %{public}@
Claim %{public}@ was cancelled before claimer was invoked
A server unexpectedly received a saveChangesWithCompletionHandler: message
Change, deletion, or movement of %{private}@ interpreted as change
Range %{public}@ of string with length %lld -- determined final disambiguation hints: %lld.
*** NSKeyedArchiver warning: replacing existing value for key '%@'; probable duplication of encoding keys in class hierarchy
It is insecure to set the archived object class name. The class name provided will be ignored: %{public}@. Please use .archivedObjectClass instead and do _NOT_ use NSClassFromString(…) unless you are matching the class to an allow-list.
Load resulted in a URL (%@) and a copied file was requested; NSItemProvider will copy the contents of the file to a temporary directory
Starting to observe state of client with pid %d on behalf of claim %{public}@
Service %{public}@ succeeded in preparing file %{private}@ for uploading. Resulting path: %{private}@
NSFileCoordinator: A subarbiter was told by a superarbiter to start subarbitrating twice, which is a surprise.
-[NSFileVersion removeAndReturnError:]: You can't use it with a non-local version.
Malformed loctable (strings) at %s: %@
NSInflect attribute is an inflection rule (%@ / %@), using it in range %{public}@
Cannot use inflection engine (Obtaining the first token): %{public}@
Unexpected state upon completion of conditionallyBeginAccessingResourcesWithCompletionHandler (error handler) (%lld)
Read (Subarbitration) options: %lx -- URL: %{private}@ -- purposeID: %{public}@ -- claimID: %{public}@
Denying access for claim %{public}@ because the presenter (reactor ID: %{public}@) performing it has been disconnected
%{public}@ finished savePresentedItemChanges
%{public}@ finished accommodateEviction
Cannot find executable for bundle %{private}s %{private}s
struct URL no longer stores an NSURL. Clients should not assume the memory address of a URL will contain an NSURL * or CFURLRef and should not send ObjC messages to it directly. Bridge (url as NSURL) instead.
Could not find a term of address string in range %{public}@ that is compatible with language %{public}@.
<NSItemProvider %{public}p> Cannot determine expected value class in an NSItemProvider secure coding item completion handler. Falling back to returning the default class.
claim %{public}@ is re-evaluating after resolving a symlink
Failure to acquire UID from fault xattrs: %@
NSFileVersion couldn't find the library for a file. URL: %@
#vnode path: %{private}@, flags: %p
There was an error parsing the Info.plist at path %{private}s/%{private}s: %{public}s - %{public}ld
Error loading %{private}s: %{private}s
Cannot use inflection engine for language %{public}@ (Getting the dictionary for this locale): %{public}@
Cannot use inflection engine (Obtaining the lemma mappings for a morphological word token): %{public}@
Load handler provided a local file at %@ that should not be opened in-place, NSItemProvider will vend a temporary copy created at %@
A subarbiter is being asked to grant a claim (%{public}@) by something other than its superarbiter, which is a surprise.
A server unexpectedly received a observeDisconnection message
%{public}@ finished accommodateDeletion
%@: attempt to deallocate static bundle - break on _NSBundleDeallocatingStaticBundle to debug. This bundle %p would have been overreleased, but will instead be preserved.\n\tBundle Identifier: %@\n\tBundle URL: %@
NSPredicate: Using NSConstantValueExpression on a Class '%{public}@' is deprecated and will be removed in a future release.  NSConstantValueExpression should operate on instances.
NSPredicate: Invalid argument passed to NSFunctionExpression with selector '%@' and parameter encoding '%s' expecting pointer
Cannot use inflection engine (Casting a token to obtain a morphological word token): %{public}@
A file presenter is being asked to reacquire from a writer more times than it's been asked to relinquish
-[NSFileAccessNode urlOfSubitemAtPath:plusPath:] is returning nil.
NSFileVersions's invocation of -[NSFileManager URLForDirectory:inDomain:appropriateForURL:create:error:] returned nil for NSAutosavedInformationDirectory. Here's the error:\n%@
<NSProgressSubscriber %p> Start for ID %{public}@ URL %{private}@
Ensure bundle exists failed for path %{private}s
NSTask: Failed to spawn task due to receieving EAGAIN many times despite retrying; this means the system could not spawn a new process.
Could not find SecTaskCopySigningIdentifier symbol
A subarbiter is being notified of file prsenter tying it's not even subarbitrating yet, which is a surprise.
A server unexpectedly received a observeSharingChangeWithSubitemURL: message
Asking presenter %{public}@ to relinquish to claim %{public}@ via %{public}s
marking version %@ for %@ as resolved failed. The error is:\n%@
Stopping watcher for %{private}@
Registering static factory %{public}s %{public}s.
URL %@ is not a file:// URL.
Killing %d because it was suspended before replying to an NSFilePresenter method
Unable to create NSItemProvider temporary directory
Claim %{public}@ is blocked waiting for claim %{public}@ to finish.
Making presenter %{public}@ validatePresentedItemDeletion
%{public}@ cancelled providing by %{public}@
%{public}@: received an undecodable message (invocation with bad argument info)
<NSItemProvider %{public}p> Ignoring registration of class %{public}@ because it does not conform to the NSItemProviderWriting protocol.
KVO ISSUE: %{public}@ -- Has called 'will' or 'did' for the same key in multiple threads, first will/did recorded in thread %{public}@ -- in thread: %{public}@, backtrace: %{public}@
NSPredicate: Using NSExpression CAST(x,'%{public}@') is deprecated and will be removed in a future release.  '%{public}@' should not be cast into the unknown type '%{public}@'
Destroying process monitor for pid %d
Claimer for %{public}@ is waiting for provider %{public}@ to provide
Connection to filecoordinationd interrupted. Client has providers, but not re-adding them because _setAutomaticFileProviderReregistrationDisabled:YES was called.
Presenter %{public}@ relinquished
Presenter %{public}@ detected non-coordinated event
There was an error parsing the Info.plist for the embedded property list in the bundle at path %{private}s: %{public}s - %{public}ld
NSBundleResourceRequest encountered a sandboxing error (extensions): %d
%{public}@ blocked pending grantAccessClaim
A server unexpectedly received a observePresenterChange: message
%{public}@ finished reportUnsavedChanges with reply: %s
NSFileCoordinator does not handle NSURLs that return relative paths when sent -path, like this one:\n%{private}@
Subarbitration claim %{public}@ granted in client
%{public}@: received an undecodable message (invocation with bad replaced by pointer argument)
Letting claim %{public}@ go before blocking claim %{public}@ because the latter is blocked by a reactor with the former's purposeID: %{public}@
%{public}@ received grantAccessClaim reply
Added provider %{public}@
<NSItemProvider %{public}p> Unable to find a suitable representation to instantiate class
<NSItemProvider %{public}p> Selector-based coercion failed with error: %@
'%{public}@' should not be used to for un-archiving and will be removed in a future release
Preventing suspension of pid %d for activity: %{public}@
Forwarding pending claim %{public}@ to subarbiter for claim %{public}@ for evaluation there
-[NSFileVersion replaceItemAtURL:optionsError:] for a non-local NSFileVersion failed. Did you forget a coordinated read?
%@ received data before consuming
%{public}@ -- Checking for consistency now (%{public}@).
Further suppressing excessive logging
%{public}@ grantAccessClaim reply is an error: %{public}@
Making presenter %{public}@ validate subitem relinquishment for URL: %{private}@
-[NSXPCConnection valueForEntitlement:]: Error getting value for entitlement '%{public}@': %{public}@
Unable to load main bundle: Unable to create main bundle URL from %s
NSPredicate: NSKeyPathExpression: malformed selector
Registering provider %{public}@ disallowed. Only file URLs are allowed, unlike this one: %{private}@
%@ overrode the default implementation of '-decodeValueOfObjCType:at:', which is insecure and deprecated, but not '-decodeValueOfObjCType:at:size:' which is insecure as it can lead to potential buffer overflows. Use the safer '-decodeValueO
interaction_tracking
Error occurred while asking fileproviderd (%d) to prepare providers: %{public}@
Nullified subarbitration claim %{public}@ to work around a deadlock with claim: %{public}@
Forwarding claim %{public}@ to subarbiter for claim %{public}@ for evaluation there
There was an error parsing the Info.plist for the bundle at path %{private}s/%{private}s: Could not convert to file system representation
*** Assertion failure in %@, %@:%ld
<NSItemProvider %{public}p> Load result contained a data blob that failed to unarchive as a %{public}@
Removing temporary folder at %@ created to provide a copied file or file representing data for the loader
As requested, cancelling claim %{public}@ because it is blocked by claim %{public}@.
[NSFileAccessNode assertLive] found a surprisingly dead node.
#fsevents Starting stream for %{private}@ with event ID %llx
Current locale fetched with overriding locale identifier '%{public}s' which does not have a country code
User morphology preferences value read from the protected domain: %@ (is present? %{public}s)
Claim %{public}@ was devalued
Making presenter %{public}@ accommodateDeletion
Making presenter %{public}@ observe change
-[NSError init] called; this results in an invalid NSError instance. It will raise an exception in a future release. Please call errorWithDomain:code:userInfo: or initWithDomain:code:userInfo:. This message shown only once.
Range %{public}@ of string with length %lld -- edited target inflection with attributes from replacements that are unambiguous adjectives: %@.
%@: warning: NSKeyedArchiver deallocated without having had -finishEncoding called on it.
%{public}@ was probably made on an already-cancelled NSFileCoordinator instance (%p). It will be immediately cancelled before being sent to the server.
Making presenter %{public}@ observe presenter change: %d at %{private}@
%{public}@: Warning: Exception caught during invocation of selector %{public}s, dropping incoming message and invalidating the connection.\nException: %{public}@\n%{public}@
`NSPointerArray` should not be used in archives.
(ReadingForUploading) Creating zip archive of coordinated directory
Waking up fileproviderd (%d) to prepare providers
Not waiting for reacquisition reply for presenter %{public}@ after claim %{public}@
-[NSFileAccessNode standardizedURL] is returning nil.
%{public}@: Exception caught during invocation of reply block to message '%{public}s'.\n\nException: %{public}@
Lookup of 'AppleLanguages' from current preferences failed lookup (app preferences do not contain the key); likely falling back to default locale identifier as current
NSPredicate: Using NSCustomPredicateOperator on a Class '%{public}@' is deprecated and will be removed in a future release.  NSCustomPredicateOperator should operate on instances.
Service %{public}@ failed to prepare file %{private}@ for uploading. Error: %{private}@
New subarbitration claim %{public}@ is blocked by subarbitration claim %{public}@
dlsym found symbol %s
Cannot initialize analyzer factory: %{public}@
<NSItemProvider %{public}p> Archiving the provided object failed with an exception: %@
Claimer for %{public}@ is waiting for provider %{public}@ to provide a physical URL
Received item sharing change hint with purpose %{public}@ -- %{private}@
Registering provider %{public}@ disallowed. Process %d is not allowed to access the requested path or any of its parent directories: %{private}@
NSBundle %@ principal class is using first class name %@ because the bundle has no principal class name
NSFileProviderMessenger's proxy factory returned an error: %{public}@
NSInflect attribute is YES, using automatic inflection in range %{public}@, initial target: %@, language-specific rules: %@ (%@)
<NSItemProvider %{public}p> Loading in-place representation for type failed with error: %@
%{public}@ -- No longer tracking for consistency changes.
KVO ISSUE: %{public}@ -- Has called 'did' more times than 'will' -- in thread: %{public}@, backtrace: %{public}@
AppKit called rmdir(\"%@\"), it didn't return 0, and errno was set to %i.
*** malloc returned NULL in NSUnitFormatter! Tried to allocate %zu bytes
There was an error parsing the Info.plist at path %{private}s: %{public}s - %{public}ld
<NSItemProvider %{public}p> Expected class is not a URL; attempting to load the object and coerce to the expected class
A process invoked -[NSFileCoordinator prepareForReadingItemsAtURLs:options:writingItemsAtURLs:options:error:byAccessor:] but filecoordinationd crashed. Invoking the batchAccessor anyway.
Re-watching for new\u00a0or moved file
Locale.current constructing a locale identifier from preferred languages by combining with set country code '%{public}s'
LocalizedStringResource contained a sandbox extension token but sandbox check passed without consuming the token. Proceeding to lookup localized string without consuming a sandbox extension.
Received item ubiquity attributes change hint with purpose %{public}@ -- %{private}@. Attributes: %{public}@
Adding provider %{public}@ for URL: %{private}@
More than one bundle with the same identifier has been added: %{public}s
RemoveInstanceForFactory: No factory registered for id %s
Useful inflection with new replacement in range %{public}@
Added presenter %{public}@
Making presenter %{public}@ accommodateEviction
Received relinquishment reply for presenter %{public}@ to claim %{public}@
Unable to set constraint %{public}@=%{public}@: %{public}@
NSBundle %@ loading failed because bundle loading is disabled
NSPredicate: NSFunctionExpression incorrect number of arguments passed to method
Creating path from components (%{private}@, lengths: %@) resulted in an embedded NUL character
Cannot derive expected value class from a NSItemProvider preview completion handler.
%{public}@ checking if moving an item within its container requires providing
<NSItemProvider %{public}p> Load handler produced an object of class %{public}@; archiving the object via NSKeyedArchiver and providing the archived data
Unexpected state upon completion of beginAccessingResourcesWithCompletionHandler (success case) (%lld)
Presenter %{public}@ has been tied to a URL for the first time -- %{private}@
Asking provider %{public}@ if moving item within its container requires providing
NSFileVersion tried to tried to delete temporary version storage and failed. Versioned file URL: %@, error: %@
Received item version change hint of kind %{public}@ with purpose %{public}@ -- %{private}@
Unable to deliver Notification to Message observer because %s.makeMessage() returned nil. If this is unexpected, check or provide an implementation of makeMessage() which returns a non-nil value for this notification's payload.
Lazy cache miss for bundle %s keys: %s table: %s
Static resource lookup for resource %{private}s %{private}s %{private}s failed - not a bundle
NSPredicate: NSCustomPredicateOperator incorrect number of arguments passed to method
NSUndoManager<%p> (main) connection for UUID %{public}@ to auxiliary manager terminated
Provider %{public}@ finished providing for %{public}@
<NSItemProvider %{public}p> Finished loading file representation for type identifier '%{public}@' with error: %@
*** uplrules_select() failed in NSUnitFormatter: %s, len = %d
Resuming normal logging
Not advancing in ordinality(of:in:for:). smaller: %{public}s, larger: %{public}s, date: %{public}f
API MISUSE: URL(filePath:) called with a \"file:\" scheme. Input must only contain a path. Dropping \"file:\" scheme.
Useful inflection but no replacement in range %{public}@
NSBundleResourceRequest could not connect to its helper daemon
Load resulted in a URL (%@) and an in-place file was requested, however an in-place read cannot be performed (readonly=%@, prefersCopy=%@); NSItemProvider will perform a coordinated read and copy the contents of the file to a temporary dire
Received item reconnection hint with purpose %{public}@ -- %{private}@
Could not load bundle to find function pointer for %s: %@
Malformed loctable (strings) at %s: missing language %s
NSBundle %@ principal class is nil because the bundle is not loaded
NSUndoManager<%p> (aux) received connection request from a main undo manager, but it is already connected to a main undo manager
NSUndoManager<%p> (aux) connection to main undo manager interrupted
<NSItemProvider %{public}p> Load handler produced the URL %@ and the type identifier '%{public}@' is not a URL; vending the URL to the contents of the data directly
Begin: Request (Conditional) 0x%p / Bundle 0x%p / Tags: \"%{public}@\"
Provider %{public}@, while providing for claim %{public}@, returned an error: %@
NSUndoManager<%p> (aux) performed %{public}@ %{public}@ triggered from remote - no %{public}@ actions registered
NSBundleResourceRequest helper daemon reports an error in parsing the on demand resources information: %@
%{public}@ finished validatePresentedItemDeletion with reply: %s
%{public}@: Exception caught during decoding of received selector %{public}s, dropping incoming message.\nException: %{public}@
KVO ISSUE: %{public}@ -- The value for this key pair seems to have changed outside of a will/did pair, which makes this key unsafe to observe within a longer key path; last observed value was '%{public}@', current value is '%{public}@'
Refusing to cancel a File Coordination-originating operation
A server unexpectedly received a observeVersionChangeOfKind: message
[NSFileAccessNode setProvider:] was invoked for a node that already has a provider (pid %d). Ignoring the new one (pid %d).
-[NSFileVersion replaceItemAtURL:options:error:] failed to remove the version that it replaced a file with.
Using fileReferenceURL for  FSEventStreamCreate() returned NULL. Path: %{private}@
%{public}@: Warning: Received reply to unknown message. Dropping incoming message and invalidating connection.
Registering for NSUbiquityIdentityDidChangeNotification without the necessary entitlements
NSUndoManager<%p> (aux) performed %{public}@ %{public}@ triggered from remote - responding with registration of %{public}@ %{public}@
Bundle: %{private}s, key: %{private}s, value: %{private}s, table: %{private}s, localizationNames: %{private}s, result: %{private}s
Making presenter %{public}@ reportUnsavedChanges
Making presenter %{public}@ observe ubiquity attributes change: %{public}@
NSFileVersion tried to tried to add a new generation and failed. Versioned file URL: %@, contents URL: %@, error: %@
Reporting non-coordinated move to %{private}@
<NSProgressSubscriber %p> Remove publisher forID: %{public}@
Warning: Language identifier is not in canonical form: %@
Object cannot be a Swift value type.
Disavowing claim %{public}@ that was never granted
Received item change hint with purpose %{public}@ -- %{private}@
NSFileCoordinator does not handle NSURLs that return nil when sent -path, like this one:\n%{private}@
Subarbitration claim %{public}@ invoked in client
Coalescing observations for both the logical URL %{private}@ and its promise URL
<NSProgressSubscriber %p> Start for ID %{public}@ category %{public}@
<NSItemProvider %p> Instantiation of class %{public}@ failed with error: %@
*** uameasfmt_open() failed in NSUnitFormatter: %s, _formatter: %p, localeID: %s, width: %u, icuNF: %p
Claim %{public}@ granted in server
Removing presenter %{public}@
There was an error parsing the Info.plist at path %{private}s/%{private}s: unable to convert to url
Not advancing Calendar enumeration result: %{public}f next: %{public}f previous: %{public}f %{public}s %{public}s %{public}s %{public}s %s
NSPredicate: Using NSCustomPredicateOperator with selector '%@' and parameter encoding '%s' is forbidden
<NSItemProvider %{public}p> Failed to copy item at %@ to temporary folder with error: %@
<NSItemProvider %{public}p> Loading NSURL object failed with error: %@
<NSItemProvider %{public}p> Loaded NSURL object %@ successfully
Unexpected state upon completion of beginAccessingResourcesWithCompletionHandler (error case) (%lld)
NSUndoManager<%p> (main) removed %lu undo actions and %lu redo actions due to invalidated connection with UUID %{public}@
Bundle %{public}s contains a factory ID which is not a string. Not registering.
Unable to load .strings file: %s / %s: Top-level object was not a dictionary
End: Request 0x%p
Will be managing connection for %{public}@ because path is not private %{private}@
*** [NSUnitFormatter stringForValue:unit:] _formatter is nil
*** uameasfmt_format() (2nd attempt) failed in NSUnitFormatter: %s, len = %d, value = %f, unit = %lu
cancelling a connection for subarbitration claim %{public}@
An arbiter is confusing itself after a file was moved while telling progress things about node replacement
Unable to find Calendar enumeration result: %{public}f %{public}s %{public}s %{public}s %{public}s %s
loctable failed to load for bundle: %s: table: %s: %@
%{public}s|%{public}s|%{public}s|%hhu
Deferring relinquishment to %{public}@ because of pre-relinquishment in progress
Starting relinquishment to claim %{public}@
Enumeration of versions for %@ failed. Here's the error:\n%@
#filereference Detected deletion of %{private}@
Overflowing in ordinality(of:in:for:). smaller: %{public}s, larger: %{public}s, date: %{public}f
NSUndoManager<%p> (aux) received a cross-process connection request from a main undo manager whose undo actions cannot merge cleanly with the auxiliary undo actions. The undo/redo stack will be cleared.
<NSItemProvider %{public}p> Performing a coordinated delete of the cloned temporary file at %@
<NSItemProvider %{public}p> Loading produced a data blob and NSItemProvider failed to coerce the data to an unarchived URL with error: %@
#fsevents path: %{private}@, flags: %x (ignored: %x), id: %llx
-[NSFileVersion removeAndReturnError:]: You can't use it with a current version.
<NSProgress %p> Publishing for URL %{private}@ in category %{public}@ with ID %{public}@
There was an error parsing the Info.plist for the bundle at path %{private}s/%{private}s: %{public}s - %{public}ld
dlfcn check load bundle %{private}s mode %d
sandboxing denied subscription to progress on category %@ (bundle id %@, %@)
<NSItemProvider %{public}p> Registering loadHandler for NSItemProviderWriting class %{public}@ with declared types %{public}@
<NSItemProvider %{public}p> Registering loadHandler for NSSecureCoding object for type identifier: '%{public}@'
Failed to get thread materialization iopolicy value: %{darwin.errno}d
Received claim %{public}@
A subarbiter was told by a superarbiter about a file disappearance, which is a surprise.
Unexpected Calendar enumeration result: start: %{public}f test: %{public}f %{public}s %{public}s %{public}s %{public}s %{public}s %s
Bundle %{public}s contains a type ID which is not a string. Not registering.
String(format:locale:arguments:): Provided argument types %{public}s (with inferred specifiers %{public}s) do not match the format string's specifiers [%@]
Range %{public}@ of string with length %lld -- edited target inflection with attributes from replacements that are other words: %@.
KVO failed to allocate class pair for name %{public}@, automatic key-value observing will not work for this class
NSUndoManager<%p> (main) is triggering remote %{public}@ of %{public}@ over connection %{public}@
<NSItemProvider %{public}p> Expected class is a URL but the type identifier '%{public}@' is not a URL, loading the type identifier and attempting to convert to a URL
Begin: Request 0x%p / Bundle 0x%p / Tags: \"%{public}@\"
NSPredicate: NSFunctionExpression no longer allows arbitrarily long parameter lists
NSUndoManager<%p> (main) registering local %{public}@ %{public}@ linked to remote %{public}@ action from connection %{public}@
Unexpected state upon completion of conditionallyBeginAccessingResourcesWithCompletionHandler (available case) (%lld)
Presenter %{public}@ has finished relinquishing, unblocking claimer for %{public}@
Received a request to grant an access claim, but received no access claim instance.
[NSFileAccessNode pathToDescendantForFileURL:componentRange:] was invoked in a surprising way.
<NSProgress %p> Unpublishing %{public}@
Cannot use inflection engine for language %{public}@ (Setting the tokenizer to use the unmodified style): %{public}@
<NSItemProvider %{public}p> No item found conforming to type identifier '%{public}@'
A subarbiter is being notified of item disconnection, which is a surprise.
Prerelinquishment already in progress. Adding a new prelinquishment reply
Detected content change to %{private}@
#fsevents FSEventStreamCreate() returned NULL. Path: %{private}@
CFBundle Performance: File cache hit  : %s
Inflection was identity; assumed inflection attribute value %{public}@ will be used instead in range %{public}@
Encountered write failure %d %s
<NSItemProvider %{public}p> Load handler failed with error: %@
%@: Skipped decoding bookmark data due to NSKeyedUnarchiver mode.
Taking assertion for %{public}s while sending it an NSFilePresenter message
Suppressing excessive logging
%@
Range %{public}@ of string with length %lld has a format specifier or external dependency; not inflecting during preflight.
NSUndoManager<%p> (aux) connection to main undo manager invalidated
Ignored new presenter %{public}@, because one with the same ID already exists
A subarbiter was told by a superarbiter about a file version change, which is a surprise.
A subarbiter is being notified of a ubiquity attribute change and it's not even subarbitrating yet, which is a surprise.
Making presenter %{public}@ observe version change
%{public}@ observing end of writing claim %{public}@
Subarbitration claimer %{public}@ is waiting for %{public}@ response from presenter: %{public}@
%{public}@: NSSecureCoding allowed classes list contains [NSObject class], which bypasses security by allowing any Objective-C class to be implicitly decoded. Consider reducing the scope of allowed classes during decoding by listing only th
Removing provider %{public}@
Subarbitration claim %{public}@ granted in server
Unexpected XPC error type on reply: %s
NSProgress Exception caught: %@
<NSItemProvider %{public}p> Cannot find representation conforming to type '%{public}@'
<NSItemProvider %{public}p> Loading data representation for type failed with error: %@
Claim %{public}@ forwarded to superarbiter
Presenter %{public}@ reacquired
%{public}@ asking provider %{public}@ to provide
Not explicitly asking presenter to relinquish to claim %{public}@ because it has already relinquished
%{public}@: Unexpected data on XPC connection, invalidating the connection.
<NSProgress %p> Dropped remote update for key %{public}@ due to throttling
Locale.current constructing a locale identifier from preferred languages without a set country code
Cannot use inflection engine for language %{public}@ (Getting analyzer from factory): %{public}@
Write (Async) options: %lx -- URL: %{private}@ -- purposeID: %{public}@ -- claimID: %{public}@
Making presenter %{public}@ reacquire after claim %{public}@
A subarbiter was told by a superarbiter about a sharing change, which is a surprise.
%{public}@ finished providing
Type %{public}s added to factory %{public}s
<NSProgressRegistrar %p> Add subscriber %p forID: %{public}@ for URL %{private}@
Upload preparation for claim %{public}@ completed with error: %{private}@
A server unexpectedly received a setProviderPurposeIdentifier: message
Out of range Calendar enumeration result: start: %{public}f test: %{public}f %{public}s %{public}s %{public}s %{public}s %{public}s %s
%s. Error: %s
NSPredicate: Using NSFunctionExpression with selector '%@' passed the incorrect number of arguments
<NSItemProvider %{public}p> Finished loading data representation for type identifier '%{public}@' with error: %@
Using ~%{public}s resources
AddInstanceForFactory: Added instance for id %s
NSPredicate: NSFunctionExpression unable to find method
<NSItemProvider %{public}p> Load handler failed to produce NSSecureCoding object with error: %@
<NSItemProvider %{public}p> Load handler produced the URL %@ and the type identifier '%{public}@' is a URL; archiving as an NSURL archive
udtitvfmt_open failed!  Formatter is NULL! -- locale: %s, template: %@, timezone: %@, status: %s
Removed presenter %{public}@
Failed to write filecoordinationd dump file. Received exception: %@\n%@
<NSItemProvider %{public}p> Load handler successfully provided NSItemProviderWriting object %@, calling out to -[%{public}@ loadDataWithTypeIdentifier:] to load the data representation of the object
Claim %{public}@ is not blocked by %{public}@ because it has the same purposeID: %{public}@
Claim %{public}@ failed symbolic link resolution due to an apparent link cycle
A process invoked one of the -[NSFileCoordinator coordinate...] methods but filecoordinationd crashed. Returning an error.
A server unexpectedly received a observeUbiquityChangeWithSubitemURL: message
Making presenter %{public}@ observe move to URL: %{private}@
Unable to load main bundle: Unable to create main bundle %@
 reason=%{signpost.telemetry:string1,public}@ version=%{signpost.telemetry:string2,public}@ 
<NSItemProvider %{public}p> Unable to find a suitable type to create object of class
<NSItemProvider %{public}p> Load handler produced data; providing the data directly
Unable to connect to daemon to set preservation priority
Provider %{public}@ finished, unblocking claimer for %{public}@
A subarbiter was told by a superarbiter about a ubiquity attributes change, which is a surprise.
%{public}@ responded to moving check with: %@
Not advancing in dateComponents(from:start:end:). start: %{public}f end: %{public}f component: %{public}s
Overflowing in dateComponents(from:start:end:). start: %{public}f. end: %{public}f. component: %{public}s
NSInflect attribute is NO, not inflecting in range %{public}@
%{public}@ began providing
Provider %{public}@ responded to moving check: %@
Reacquiring immediately, because there are no more claims
NSXPCListener: received error or other non-connection type in handler for listener: %{public}s
Attempted to create instance, but factory %s is not enabled
dlfcn unload bundle %{private}s
BannedSel
%{public}s|%{public}s|%{public}s|%{public}s|%hhu
<NSItemProvider %{public}p> Load result produced a value of class %{public}@ but expected a value of class %{public}@; attempting to coerce value via type coercion
<NSProgressRegistrar %p> Add subscriber %p forID: %{public}@ in category %{public}@
NSUndoManager<%p> (aux) received an in-process connection request from a main undo manager but items are present on the redo stack. The undo/redo stack will be cleared.
Making presenter %{public}@ observe disconnection
CFBundle Performance: File cache miss : %s
NSFileProviderMessenger's proxy factory encountered a connection\u00a0failure: %{public}@
Cannot find factory %s
Could not load bundle to find function pointer for %s
NSPredicate: Invalid argument passed to NSCustomPredicateOperator with selector '%@' and parameter encoding '%s' expecting pointer
NSUndoManager<%p> (aux) removing all undo actions triggered from remote
*** [nf getFormatter] failed in NSUnitFormatter: %p
AddInstanceForFactory: No factory registered for id %s
Making presenter %{public}@ observe sharing change
Attempted to decode a collection type '%{public}@' (subclass of '%{public}@') for key '%{public}@'. '%{public}@' requires its subclasses to be explicitly added to the allowed classes list but it is not present. Allowing this has been a sour
NSInflectionReferentConcept attribute in range %{public}@ is set to %{public}ld. Expected a 'TermOfAddress' concept, but found %{private}@ instead.
Target inflection after applying inflections inferred from replacements: %{public}@
KVO ISSUE: %{public}@ -- Has become reentrant ('will' called after 'did') -- in thread: %{public}@, backtrace: %{public}@
Unable to determine if provider-less fault is a directory: %@ - req: %d
Registering presenter %{public}@ disallowed. Only file URLs are allowed, unlike this one: %{private}@
Starting prelinquishment for remote deletion request
Announced move of %{private}@ to %{private}@
<NSItemProvider %{public}p> Type coercion failed with error: %@
claim %{public}@ is trying to resolve a symbolic link too early
NSBundle %@ loading failed because of an error %@
%{public}lld format specifiers are relevant (out of %{public}lld) in range %{public}@
[NSURL setIOPolicy:] getiopolicy_np failed when setting policy: %d, type: %d, scope: %d
_NSStatic_NSUnitElectricCurrent
NSKeyValueMutableArray
_NSKeyedCoderOldStyleArray
NSNotificationCenter
_NSIsNotNilTransformer
NSEmojiCheckingResult
NSFilePresenterXPCInterface
_TtC10Foundation18_CalendarGregorian
NSCheapMutableString
_TtC10FoundationP33_AE6BD10245B422606B9EE93C01570D8F21_CombineRunLoopAction
NSCharacterSet
NSCountedSet
NSMutableAttributedStringFormatting
CharacterSetAPIsSwiftShim
_NSJSONReader
NSFileAccessArbiter
NSKeyValueUndefinedSetter
NSPrivate
NSUserDefaults_NSURLExtras
_NSIsNilTransformer
NSDeserializerStream
NSNewTextSupport
NSSortDescriptorPortCoding
NSValuePortCoding
NSConstantString
_NSStatic_NSUnitEnergy
_NSStatic_NSUnitFrequency
_NSProgressProxy
NSStreamBoundPairCreationExtensions
NSConstantDoubleNumber
_TtCV10Foundation31_POSIXDirectoryContentsSequence8Iterator
_TtC10Foundation24ICULegacyNumberFormatter
_NSMutableCharacterSetBridge
NSObservationSink
_NSStatic_NSUnitElectricPotentialDifference
NSKeyValueNotifyingMutableSet
NSKeyValueObserverNotifying
NSKeyValueFastMutableOrderedSet
NSConcreteFileHandle
_NSStatic_NSUnitPower
NSRemoteUndo_Internal
_NSBundleODRDataCommon
NSPlaceholderValue
NSFileSubarbitrationClaim
NSMorphology
NSCalendar
_NSMetadataQueryResultArray
_NSURLAttributeDescriptor
NSInvocationOperation
NSArrayChangeBatch
NSProcessInfoPlatform
NSTimeZone
NSBigMutableString
NSDebugString
NSConcreteMapTableValueEnumerator
_NSPersonNameComponentsStyleFormatterShortNameSimpleFallback
_NSStatic_NSUnitLength
NSListFormatter
_NSSharedValueTransformer
NSKeyPathExpression
NSKeyValueNonmutatingArrayMethodSet
Compiler
NSSerializationSupport
NSFilePresenter
NSFileProviderInternalAdditions
_NSXPCConnectionExportedObjectTable
_NSLocalNotificationCenter
__NSObserver
NSObservationSource
NSOrthography
NSAKSerializer
NSAKDeserializer
NSXPCConnection
NSUnitConcentrationMass
NSBlockExpression
_NSInflectionRuleAutomatic
_TtC10Foundation13__JSONDecoder
_NSConcreteObservation
_NSStatic_NSUnitAngle
_NSInlineObserverList
_NSIPCallbackSerialization
NSFileCoordinationDebugInfoXPCInterface
_TtC10Foundation21_TimeZoneAutoupdating
NSIndexSet
NSSymbolicExpression
NSOrderedCollectionChange
NSInflectionRuleExplicit
NSInternalUseOnly
NSIndexPath
NSUnitElectricPotentialDifference
_NSStatic_NSUnitElectricResistance
ODRServerProtocol
_NSFileManagerBridge
_TtCVV10Foundation3URL8Template6Global
_TtC10Foundation19ICUPatternGenerator
NSXPCEncoder
NSCustomPronouns
_NSStatic_NSUnitTemperature
NSTextCheckingResult
_NSObservableObservation
NSString
NSPersonNameComponentsFormatter
NSEncodingDetectionPlaceholder
NSKeyValueNestedProperty
NSTokenMatchingPredicateOperator
NSKeyValueFastMutableArray2
NSProcessInfoHardwareState
NSItemProviderWriting
_TtCO10Foundation3ICU15StringConverter
NSDecimalNumberPlaceholder
_NSLocaleBridge
_NSOriginalAttributedString
NSURLQueryItem
_TtC10Foundation20__PlistEncoderBPlist
_NSBPlistMappedData
NSExtensionURLResult
_NSStatic_NSUnitMass
NSCFType
NSDecimalNumberBehaviors
NSUnit
NSKeyedUnarchiver
NSPredicateOperator
NSKeyValueSharedObservers
NSKeyValueNotifyingMutableArray
NSConcreteTask
_NSSharedKeySetS
_NSPersonNameComponentsStyleFormatterAbbreviated
NSCoder
NSSecurityScopedURLWrapper
NSFileProviderService
NSKeyValueCodingPrivate
NSExtension
NSURL
NSCoding
NSConcreteAttributedString
NSAutoreleasePool
NSMassFormatter
NSUserActivitySerialization
NSOwnedDictionaryProxy
NSArchiver
NSKeyValueProxyCaching
_NSThreadPerformInfo
NSPredicateVisitor
NSInternalForAppKit
NSFileProviderXPCMessenger
_NSPersonNameComponentsStyleFormatterMedium
NSMutableIndexSet
NSMetadataQuery
NSPreviewSupport
NSDateInterval
NSFileWatcherObservations
_TtC10FoundationP33_E8BADD1F7652560CB20FCE81B026A2EF33_NSBundleInfoDictionaryEnumerator
_NSBundleDidLoadNotificationPayloadArray
NSLock
NSKeyValueNilOrderedSetEnumerator
NSKeyValueIvarMutableOrderedSet
NSXPCListenerDelegate
NSBoundKeyPath
NSKeyValueCoding
NSKeyValueObservingPrivate
NSMatchingPredicateOperator
NSInflectionRule
NSPurgeableData
NSNull
_NSTimerBlockTarget
NSUndoManager
_NSUndoLightInvocation
NSExpression
NSInflection
_NSUndoManagerMainInterface
NSOrderedSetChange
NSInflectionPresets
NSProgressSubscriber
NSOperationQueue
NSQuoteCheckingResult
_NSBundleInfoDictionary
NSGrammarCheckingResult
_NSAttributedStringGrammar
_NSStatic_NSStaticUnitConverterLinear_NoConst
_Morphun
NSTernaryExpression
_NSSwiftURLQueryItem
_TtCO10Foundation10JSONFuture8RefArray
_TtC10Foundation9BPlistMap
Exceptions
_TtC10Foundation11BundleInner
_NSXPCConnectionExpectedReplyInfo
NSDataCompression
NSTimer
_NSUndoInvocation
NSCalendarDatePortCoding
_NSPersonNameComponentsStyleFormatterGivenOnlyVariant
NSLocale_LanguageExtras
NSXPCInterface
_NSClrDatM
NSSetChangeActions
__NSCFLocalizedAttributedString
NSLocale_CalendarDirection
NSMorphologyUserSettings
NSUnitPressure
_NSAssumedFallbackInflectionAttributeDescriptor
_NSAttributedStringFromMarkdown
_NSAuxiliaryUndoManagerReference
NSPredicateValidator
NSSubstitutionCheckingResult
NSFileCoordinatorUploadFilePreparing
_NSOwningMappingObservation
NSNumberFormatterUnitFormatting
NSTruePredicate
NSUniquePart
NSKeyValueIvarMutableCollectionGetter
_TtCE10FoundationCSo20NSNotificationCenter13Notifications
BPlistConvenience
NSKeyValueProxyShareKey
NSCondition
NSFileWritingWritingClaim
_NSNumberFormattingAttributeDescriptor
NSFileAccessProcessManager
NSKeyValueNotifyingMutableOrderedSet
NSFilePresenterManagedProxy
_NSPersonNameComponentsStyleFormatterLong
NSExtensionService_Subsystem
_TtC10Foundation34_NSSwiftImmortalCharacterSetBridge
NSComparisonPredicateOperator
NSSubrangeData
_NSExtensionContextVendor
NSNotification
_TtC10Foundation13__NSSwiftData
_NSStringProxyForContext
__NSLocalizedString
NSFileCoordinationSupport
_TtC10Foundation18ICUNumberFormatter
NSUnitElectricCharge
NSKeyValueMethodGetter
_NSKeyedUnarchiverHelper
NSURLFileTypeMappings
NSXPCCoder
_TtC10Foundation16ProgressReporter
_NSSwiftURLComponents
NSDateFormatter
__NSBundleTables
NSSecureUnarchiveFromDataTransformer
_TtC10FoundationP33_12768CA107A31EF2DCE034FD75B541C913__JSONEncoder
_TtC10FoundationP33_12768CA107A31EF2DCE034FD75B541C924__JSONReferencingEncoder
NSEqualityPredicateOperator
_NSBPlistMappedString
NSAttributedStringFormatting
_TtC10Foundation26__NSErrorRecoveryAttempter
_NSKVO1Adaptor
NSSpellCheckingResult
NSComplexRegularExpressionCheckingResult
NSDirInfoDeserializer
_NSSwiftCharacterSet
_TtCV10Foundation17_AsyncBytesBuffer7Storage
NSKeyValueMutatingSetMethodSet
NSKeyValueIvarMutableSet
NSURLQueue
_TtCE10FoundationCSo12NSDictionary9_Iterator
_NSStdIOFileHandle
NSAutoContentAccessingProxy
NSKeyValueMutatingCollectionMethodSet
NSPortNameServer
NSKeyValueMutableSet
NSKeyedArchivalErrors
NSInputStream
NSLinkCheckingResult
NSAttributedString
NSDecimalExtension
NSRTFD
_NSXPCDistantObject
NSPrivate_Enumeration
_NSBundleResourceRequestAppExtensionAdditions
NSAKDeserializerStream
NSAggregateExpression
NSMorphologyPronoun
NSUnitFuelEfficiency
NSKeyValueSlowMutableSet
_NSPerformanceMeter
NSKeyValueSharedObserversSnapshot
NSExtensionItem
NSRLEArray
_NSIndexSetEnumerator
NSThread
_NSJSONWriter
_TtC10Foundation23PredicateArchivingState
NSURLExtras
NSUserDefaults
_NSKeyedUnarchiveFromDataTransformer
PKModularService
_NSSwiftBundle
NSAnyKeyExpression
_NSPersonNameComponentsData
_NSStatic_NSUnitInformationStorage
NSMetadataQueryAttributeValueTuple
_TtCE10FoundationCSo20NSNotificationCenter22NotificationMessageKey
_NSObservingObservation
_NSConstantIndexSet
NSKeyValueFastMutableSet
NSExtendedRegularExpressionCheckingResult
_TtC10Foundation35__PlistDictionaryReferencingEncoder
Foundation2
_NSKeyValueObjectBox
NSSmartPunctuationController
_TtC10Foundation13__JSONEncoder
_TtC10Foundation14_LocaleBridged
NSKeyValueProxyGetter
NSConditionLock
NSConcreteSetChanges
__NSLocalTimeZone
NSLocalizableString
_NSSwiftTimeZone
NSFilterObservationTransformer
NSNotificationQueue
NSStringOtherEncodings
_TtC10Foundation9_SwiftURL
NSProgressPublisherProxy
NSObservableKeyPath
NSOldValueObservationTransformer
NSRemoteUndo
NSConcretePipe
_NSKVODeallocSentinel
_NSBundleODRDataForApplications
NSJSONSerialization
NSFileCoordinatorReacquisitionBlockCompletion
NSFilePresenterXPCMessenger
_NSPlaceholderObservation
NSKeyValueFastMutableSet2
NSArrayChange
_NSStringFormattingOptions
NSKeyValueAccessor
NSPlaceholderMutableString
_NSPersonNameComponentsStyleFormatterFamilyOnlyVariant
NSUnitFormatter
NSXPCConnectionExtensions
__NSVariableWidthString
NSNullFileHandle
NSRunLoop
NSConcreteSetChange
NSFileProviderMovingInfo
NSKeyValueMutableOrderedSet
NSFileVersion
NSProgressPublisher
_NSStatic_NSUnitElectricCharge
NSKeyValueMutatingOrderedSetMethodSet
NSCFOutputStream
NSDiscardableContent
NSDecimalNumberHandler
NSProtocolChecker
_TtC10Foundation22ICUNumberFormatterBase
NSKeyValueSlowSetter
_NSFileWatcherDirectoryFileHandleInfo
NSArrayPortCoding
_TtC10Foundation51_NotificationCenterActorQueueManagerNSObjectWrapper
__NSCFCalendar
NSDocumentSerializer
NSNullPortCoding
_NSPersonNameComponentsFormatterData
_TtC10Foundation22_TimeZoneSingleDSTRule
NSRemainingString
ODRClientProtocol
NSDirectoryEnumerator
_NSStatic_NSUnitDispersion
NSConcreteArrayChanges
_NSBundleBridge
_NSUndoActionInfo
NSURLSessionDataDelegatePrivate
NSSecureCoding
NSCFError
NSMetadataQueryPrivate
_NSObserverList
Foundation4
_NSOwningObservingObservation
NSMutableStringProxyForMutableAttributedString
NSMorphologyUserSettingsInternal
_NSZeroData
NSMapTable
NSMessagePort
_NSUndoStack
NSSortDescriptor
_TtC10Foundation29ICUMeasurementNumberFormatter
NSProgressRegistrar
_NSAutoCalendar
FPFileProviderRequestProxyCreating
NSKeyValueContainerClass
NSKeyValueObservationInfo
NSEncodingDetector
NSAKSerializerStream
_NSKeyValueObservation
NSURLKeyValuePair
NSRegularExpressionCheckingResult
NSKeyValueObserving
NSConcreteOrderedSetChanges
NSURLPrivate
NSDocInfo
_TtC10Foundation24__PlistDictionaryEncoder
NSMutableOrderedSetDiffing
NSDecimalNumberScanning
NSOrderedSetChanges
NSBoundedByPredicateOperator
NSFileProviderKernelPartialFolderMaterializationInfo
NSRecursiveLock
_NSLexiconMorphunDictionary
NSFilePromiseWriteToken
NSRegularExpression
NSNaturalLanguageDate
NSMachBootstrapServer
_NSExtensionAuxHostingBase
NSDateComponentsFormatter
_NSOrderedCollectionDifferenceMoves
ErrorConvenience
NSFileWrapper
NSMeasurement
_NSPersonNameComponentsStyleFormatterAvatar
NSComparisonPredicate
NSAllDescendantPathsEnumerator
_NSStatic_NSUnitIlluminance
_NSStringAttributeDescriptor
NSSimpleCString
_TtC10Foundation4_URL
NSFileManager
NSKeyValueNotifyingMutableCollectionGetter
NSLinguisticTagger
NSXPCListener
Foundation7
NSGeometryCoding
NSKeyValueSet
_TtC10Foundation12_ProcessInfo
NSUnitElectricCurrent
NSDocumentDeserializer
NSMultiReadUniWriteLock
NSKindOfAdditions
_NSUndoManagerMainExportedObject
_TtC10Foundation17SubprogressBridge
NSTermOfAddress
NSFileWatcher
_NSPersonNameComponentsStyleFormatterShort
_NotificationCenterActorQueueManager
_NSCalendarBridge
NSCalendarDateStuff
NSCompoundPredicateOperator
NSNotificationPortCoding
NSKeyValueMutatingArrayMethodSet
NSKeyValueFastMutableCollection2Getter
NSKeyedUnarchiverObjectSubstitution
_NSUndoBeginMark
NSTextCheckingResultCreation
_NSKVOCompatibilityShim
NSAttributedStringMarkdownSourcePosition
NSKeyValueOrderedSet
_NSXPCConnectionExpectedReplies
NSAttributedStringFormattingSPI
NSUnitElectricResistance
NSXMLParser
NSHTTPCookiePortCoding
NSFileAccessNode
_NSXPCConnectionImportInfo
NSMeasurementFormatter
NSUnitAngle
_TtC10Foundation12URLParseInfo
Foundation6
NSNumberCompatibility
NSPathUtilities
NSPathStore2
NSConcretePointerArray
NSURLUtilities
NSAssertionHandler
_TtC10Foundation20_PropertyListDecoder
_TtC10Foundation17ImageLoadListener
NSReduceObservationTransformer
NSAttributedStringPortCoding
NSDataPortCoding
FileProvider
_TtCO10Foundation10JSONFuture9RefObject
NSCFAttributedString
NSCompoundPredicate
NSKeyValueArray
NSAttributedStringMarkdownParsingOptionConveniences
NSFileProviderKernelFileMaterializationInfo
_TtCC10Foundation22ICUNumberFormatterBase12FormatResult
NSInPredicateOperator
NSPersonNameComponentsInternalAdditions
_NSStatic_NSUnitDuration
_NSPlaceholderIndexSet
NSSerializerStream
NSInvocationDebugDescription
NSUnitLength
_NSAttributedStringReplacement
NSObjectPortCoding
_TtC10Foundation25ICUPercentNumberFormatter
_NSStatic_NSUnitPressure
NSStringPredicateOperator
NSTransitInformationCheckingResult
_NSXPCBoost
_NSSwiftProcessInfo
_TtCO10Foundation3ICU10Enumerator
NSUnarchiver
NSUnitMass
NSPredicateSupport
NSUndoManagerProxy
_NSConcreteDateInterval
NSKeyValueFastMutableOrderedSet2
_TtC10Foundation17__PlistEncoderXML
NSConcreteMutableAttributedString
NSValue
NSOwningObserver
NSUnitDuration
NSOutputStream
NSTask
NSIndexSetPortCoding
NSFileProvidingInfo
FoundationSwiftAdditions
NSBundleResourceRequestAdditions
UIKit_PKSubsystem
_NSSwiftCalendar
NSKeyedArchiver
NSMutableCopying
DefaultObservationImplementations
NSMessagePortNameServer
NSValueTransformer
_NSAttributedStringFromMarkdownCreatorConcrete
NSByteCountFormatter
_TtCO10Foundation15AttributeScopes25_DefaultScopeRegistration
NSURLSessionTaskDelegate
NSDimension
NSISO8601DateFormatter
_NSFileAccessAsynchronousProcessAssertion
NSFileCoordinatorAccessorBlockCompletion
_
NSArrayChanges
_NSFCUncancellableBlockOperation
NSItemRepresentationLoadResult
_NSStatic_NSDecimalNumber
NSFileProviderPrivateAdditions
_TtC10Foundation21_CalendarAutoupdating
NSProcessInfo
_NSKeyValueDidWillStats
NSObservationBuffer
NSUserActivity
NSStringPortCoding
NSXPCProxyCreating
NSDirInfo
NSFunctionExpression
NSUnitConverterReciprocal
NSFileProviderKernelMaterializationInfo
_TtC10FoundationP33_BB206CA0B38724D56C5B55865D7B7E0231__PlistReferencingEncoderBPlist
_TtC10Foundation16_TimeZoneBridged
NSMutableRLEArray
NSMorphologyConversionInternal
NSConcreteHashTable
NSObservationTransformer
NSSetChange
NSUnitFrequency
NSKeyPathSpecifierExpression
_NSActivityAssertion
NSThreadPerformAdditions
NSFileAccessClaim
NSPageData
NSDeprecatedKeyValueObservingCustomization
NSMetadataItem
NSAttributedStringMarkdownParsingOptions
_NSPlaceholderCharacterSet
NSConstantValueExpression
NSKeyValueFastMutableArray1
NSKeyValueObservingCustomization
_NSKeyValueDebugging
NSBundleExtensionMethods
NSMutableString
NSTextCheckingKeyEvent
NSCFInputStream
_TtCV10Foundation12_FTSSequence8Iterator
_NSProgressSubscriber
NSURLExtrasInternal
NSUnitEnergy
NSKeyValueNonmutatingCollectionMethodSet
NSAttributedDescriptorForAttributeKey
NSSet
NSOrderedCollectionDifference
NSDictionary
NSNotificationObservable
NSFileAccessArbiterXPCInterface
_NSObservableKeyPathChangeAdaptor
NSPointerFunctions
NSError
NSFastEnumeration
NSBundleResourceRequest
NSKeyValueSorting
NSXPCDecoder
_TtC10Foundation26ICUCurrencyNumberFormatter
Foundation5
_TtCE10FoundationCSo12NSURLSession11CancelState
NSObserverKeyPath
_TtC10Foundation15ProgressManager
NSUnitConverter
NSZString
NSConcreteScanner
_TtC10Foundation18_LocaleUnlocalized
NSMutableData
NSVendorSupport
NSDistributedNotificationCenter
NSProcessInfoActivity
NSOrthographyCheckingResult
NSFileProviderMovingResponse
_NSStatic_NSUnitConcentrationMass
NSKeyValueShareableObservanceKey
NSExtensionContext
NSTimeZonePortCoding
_TtC10Foundation13__DataStorage
NSEnglishPronounAutocomplete
_NSMetadataQuerySortingPseudoItem
NSSetChanges
NSFileReadingWritingClaim
NSFileAccessSubarbiter
_TtCV10Foundation4Data14RangeReference
_TtC10Foundation16ICUDateFormatter
_TtCO10Foundation3ICU12FieldPositer
_TtC10Foundation10_LocaleICU
NSRelativeDateTimeFormatter
_NSMetadataQueryPrivateIvars
NSArrayChangeActions
NSPointerArray
_NSLocalizedStringResourceSwiftWrapper
NSObservation
_NSStatic_NSUnitConverterLinear
_NSStatic_NSUnitSpeed
NSArrayPathExtensions
NSDelayedPerforming
NSPlaceholderString
_NSURLQueryItemBridge
_TtC10Foundation24ICURelativeDateFormatter
_TtCCE10FoundationCSo16NSOperationQueueP33_0ECEE0A75E2DD5EDFED9A6FEB26D5D3219DelayReadyOperation19CancellationContext
NSStringEncodingDetection
_NSJSONRoundTrippingNumber
NSFileProviderProxy
_NSDispatchData
Foundation3
NSNumber
NSPhoneNumberCheckingResult
_NSNegateBooleanTransformer
NSFileProviderXPCInterface
NSObservationSupport
NSFileAccessIntent
NSFileWritingClaim
NSProgressValues
NSURLError
_NSNestedDictionary
_NSStatic_NSUnitAcceleration
NSObservedValue
NSConcreteOrderedSetChange
NSAddressCheckingResult
NSFileHandle
_NSMetadataItemPrivateIvars
__NSPlaceholderURLQueryItem
NSUUID
_TtC10FoundationP33_6DA0945A07226B3278459E9368612FF427__KVOKeyPathBridgeMachinery
_NSDataCompressor
NSPersonNameComponents
NSKeyValueNonmutatingSetMethodSet
NSPredicate
NSPinyinString
NSBlockPredicate
NSKeyValueChangeDictionary
_TtC10FoundationP33_D9EE12013FCAF298EFDC142C520A690815JSONDecoderImpl
_TtCC10Foundation36_NotificationCenterActorQueueManager14StateReference
NSConcreteMutableData
_NSBundleODRTag
NSConcreteValue
NSConcreteObservationBuffer
NSFileProvidingResponse
NSURLPathUtilities
NSFileAccessClientLocalArbiterInterface
NSKeyValueSlowMutableArray
NSKeyedGeometryCoding
NSStream
NSConstantFloatNumber
NSURLDirectoryEnumerator
NSSelfExpression
NSKeyValueProperty
NSDictionaryPortCoding
_TtC10FoundationP33_1935C07EE287982D980AA89BB85ACEFA28URLSessionAsyncBytesDelegate
NSObserver
_NSBundleODRDataForExtensions
NSCustomPredicateOperator
NSFileCoordinationRetainedAccess
NSArchiverCallBack
NSMapObservationTransformer
NSConcreteMapTable
NSPropertyListSerialization
NSXPCConnectionDelegate
_TtC10Foundation11_BridgedURL
NSMetadataQueryResultGroup
NSProxy
NSOrderedPerforming
NSConcreteData
_NSInlineData
NSDashCheckingResult
NSMachPort
NSKeyValueShareableObservationInfoKey
_TtC10Foundation20_TimeZoneICUResource
NSObservable
NSBlockObservationSink
NSUnitDispersion
NSArrayConveniences
NSItemProviderReading
_NSKeyValueDebuggingDeallocSentinel
NSUnitAcceleration
NSUnitPower
NSURLSessionDataDelegate
NSFileAccessArbiterProxy
_TtC10Foundation12_TimeZoneICU
NSAutoLocale
_TtCO10Foundation15_FileOperationsP33_0F974932CC9FBACA904761811306102318_FileRemoveContext
Foundation1
NSSimpleAttributeDictionaryEnumerator
NSFileAttributes
NSMutableArray
NSKeyValueUnnestedProperty
NSScanner
_NSFileAccessClaimPresenterRelinquishment
NSSimpleAttributeDictionary
NSCFAdditions
NSClassicMapTable
NSFileAccessProcessMonitor
_NSPersonNameComponentsStyleFormatterNicknameVariant
NSArray
NSMutableDataCompression
NSCorrectionCheckingResult
NSTextDocumentPboard
NSData
NSDateIntervalFormatter
NSCalendarDate
Private
_NSObservingBlockSinkObservation
Inflection
NSFormatter
NSKeyValueIvarGetter
_NSItemProviderTypeCoercion
NSURLPromisePair
NSFilePresenterProxy
NSUnitConverterLinear
NSKeyValueIvarSetter
NSLocale
_NSUnarchiveFromDataTransformer
NSSimpleOrthography
NSInternal
_TtC10Foundation24ICUDateIntervalFormatter
_NSStatic_NSUnitVolume
_NSMorphologyAttributeDescriptor
NSMorphologyCustomPronoun
NSArrayDiffing
_NSXPCRemoteTransport
__NSSKGraphE
_NSKeyValueObjectAndKeyPair
NSKeyValueSetter
_NSAttributedStringFromMarkdownCreator
_NSInflectionRuleExplicit
_NSXPCAllowListHolder
NSMorphologyUserSettingsPrivate
_NSKVOCompatibility
NSURLComponents
NSUserInflection
NSMorphologyInternalGrammemes
__NSLocalizedStringAddition
_NSStatic_NSUnitArea
_NSLocalizedNumberFormatRuleAutomatic
NSEnergyFormatter
_NSUUIDBridge
NSExtendedStringPropertyListParsing
_NSImmortalCharacterSetBridge
NSURLPromisedItems
NSKeyValueObservance
_NSInflectionAttributeDescriptor
NSURLSessionDelegate
NSBlockOperation
NSVariableAssignmentExpression
NSConstantIntegerNumber
NSKeyedArchiverObjectSubstitution
NSCharacterSetPortCoding
_TtC10FoundationP33_D42CEAF0407E018EB9F5C9FB647D3C2912HeaderHolder
_TtC10Foundation7IOActor
NSUnitIlluminance
NSLocale_Properties
NSSetExpression
NSFilePresenterOperationRecord
_NSXPCConnectionClassCache
_NSProgressWithRemoteParent
_NSClrDat
NSException
UAUserActivityDelegate
NSUserActivityLaunching
NSUserActivityReminders
_TtC10Foundation12_CalendarICU
NSConcretePointerFunctions
NSSubstringPredicateOperator
NSPortMessage
NSProgress
NSUnitInformationStorage
_NSUndoManagerAuxiliaryInterface
NSFileReactorProxy
NSFalsePredicate
_NSConcreteBlockSinkObservation
NSUnitSpeed
NSKeyValueSlowGetter
_NSURLComponentsBridge
NSUbiquitousKeyValueStore
NSProgressReporting
_NSClStr
_TtC10Foundation27ICUByteCountNumberFormatter
_TtC10Foundation16ICUListFormatter
_TtCO10Foundation3ICU7CaseMap
NSMutableCharacterSet
_TtCC10Foundation21NSKeyValueObservationP33_6DA0945A07226B3278459E9368612FF46Helper
__NSPlaceholderURLComponents
_TtC10Foundation22ProgressReporterBridge
NSExternalRepresentation
NSHashTable
NSDateCheckingResult
NSTemporaryCompatibility
NSBundle
_NSPredicateUtilities
NSReplacement
NSDirInfoSerializer
NSMatching
NSPresentationIntent
_TtC10Foundation16_CalendarBridged
NSKeyValueSlowMutableCollectionGetter
NSLikePredicateOperator
NSConcreteNotification
NSCFStreamWeakDelegateWrapper
NSUserActivityAppLinks
_TtC10Foundation7JSONMap
_TtC10Foundation11XMLPlistMap
NSBackgroundActivityScheduler
NSWeakObjectValue
_TtCV10Foundation3URL21UnicodeLookalikeTable
NSURLHostNameAddressInfo
NSPlaceholderNumber
NSExceptionPortCoding
NSBetweenPredicateOperator
_NSStatic_NSUnitFuelEfficiency
_NSTimeZoneBridge
_NSNumericAttributeDescriptor
_NSBarrierOperation
_NSFileAccessAsynchronousProcessAssertionScheduler
NSDatePortCoding
Foundation
_NSCloudSharingDescriptor
NSUserInformation
NSKeyValueNonmutatingOrderedSetMethodSet
NSConcreteProtocolChecker
NSSimpleRegularExpressionCheckingResult
NSFilePresenterAsynchronousOperation
OS_os_transaction
_TtCE10FoundationCSo16NSOperationQueueP33_0ECEE0A75E2DD5EDFED9A6FEB26D5D3219DelayReadyOperation
NSCopying
NSLocalizedAttributedString
_NSUndoManagerAuxiliaryExportedObject
NSDataDetector
NSUnitTemperature
NSLocalizedNumberFormatRule
NSComplexOrthography
NSKeyValueSlowMutableOrderedSet
_NSFileWatcherFileHandleInfo
_TtCV10Foundation26_DarwinSearchPathsSequence8Iterator
NSCFCharacterSet
NSKeyValueObserverRegistration
_NSOperationQueueProgress
NSRegularExpressionSupport
NSSetPortCoding
_TtC10Foundation19_LocaleAutoupdating
_TtC10Foundation12_TimeZoneGMT
NSMutableArrayDiffing
__NSOperationInternalObserver
NSFileProviderPresenterInfo
_TtCVE10FoundationCSo12NSURLSession10AsyncBytesP33_1935C07EE287982D980AA89BB85ACEFA8_Storage
NSErrorPrivate
_NSMappingObservation
NSClassicHashTable
NSKeyValueFastMutableSet1
NSCFInputStreamAdditions
NSAffineTransform
_NSObservableKVO1Adaptor
NSOperation
_NSBundleOnDemandResourceClientExportedObject
NSItemProviderRepresentation
Filtering
_TtCV10Foundation21_BPlistEncodingFormat9Reference
_NSPresentationIntentDirtying
_NSXPCTransport
NSObject
NSDate
NSCFTimer
NSFileReadingClaim
_TtCE10FoundationCSo7NSTimer14TimerPublisher
NSReplacementCheckingResult
NSFileCoordinator
_NSXPCConnectionRequestedReplies
_TtCV10Foundation16AttributedString4Guts
_TtCVE10FoundationCSo20NSNotificationCenter16ObservationTokenP33_C451B686E0AF46B87E3438E7FBD7476E35_NSNotificationObserverTokenWrapper
_TtC10Foundation20_PropertyListEncoder
NSCompletionCheckingResult
NSInflectionAvailability
NSDecimalNumberExtensions
NSKeyValueFastMutableCollection1Getter
_NSUndoBlockInvocation
NSFileProviderMessageInterface
NSMutableArrayOverrides
NSSubqueryExpression
_TtCO10Foundation3ICU14ResourceBundle
_NSLocalizedStringResource
NSUnitVolume
NSConcreteArrayChange
NSPort
NSVariableExpression
NSSmartQuoteOptions
NSFilePresenterResponses
NSMethodSignatureComparison
_TtCC10FoundationP33_6DA0945A07226B3278459E9368612FF427__KVOKeyPathBridgeMachinery9BridgeKey
NSDecimalNumber
_NSPersonNameComponentsStyleFormatterShortVariantGeneral
_TtC10Foundation24__PlistDictionaryDecoder
NSDiscardableContentProxy
_NSMainThread
_NSUndoObject
_NSPredicateOperatorUtilities
_NSAttributedStringGrammarInflection
NSUserActivityPrivate
NSOrderedSet
NSUnitArea
_NSMetadataQueryExtensions
_NSKeyValueReturnedValueConsistencyStats
CSSearchableItemAttributeSet
NSProgressSubscriberProxy
_NSMarkdownStringAttributeDescriptor
NSKeyValueFastMutableArray
NSAttributedMarkdownParsing
_NSPersonNameComponentsStyleFormatterFamilyInitialVariant
_TtC10FoundationP33_45BFD3D387700B862E3A7353B97EF7ED21__CharacterSetStorage
_NSCallStackArray
NSURLQueueNode
NSLinguisticAnalysis
_NSPlaceholderData
KVOKeyPathSupport
NSPipe
NSKeyValueIvarMutableArray
NSKeyValueObserverNotification
_NSAttributeDescriptor
NSRemoteUndo_XPCListenerDelegate
NSItemProvider
_TtC10Foundation11BundleOuter
NSFileProviderMessenger
_NSThreadData
_NSUndoEndMark
NSFilePresenterRelinquishment
_NSPersonNameComponentsStyleFormatter
_NSSwiftLocale
NSMutableAttributedString
NSMetadataStitching
NSOrderedSetDiffing
NSLocking
NSErrorPortCoding
_TtC10Foundation16NSProgressBridge
_TtC10Foundation15_TimeZoneGMTICU
NSKeyValueMethodSetter
NSKeyValueNilSetEnumerator
NSLookupMatch
NSMutableSet
NSSocketStreamCreationExtensions
NSUTIPredicateOperator
NSLengthFormatter
NSFileMultipleAccessClaim
_NSPersonNameComponentsStyleFormatterGivenInitialVariant
NSEncodingDetectionBuffer
_TtC10Foundation13_CharacterSet
NSKeyValueComputedProperty
_NSBundleResourceRequestAppExtensionProtocol
NSCFOutputStreamAdditions
NSKeyValueFastMutableOrderedSet1
_TtC10FoundationP33_9C63FCD83980F3EB054FB42D4F47924E28__PlistReferencingEncoderXML
__NSConcreteUUID
NSMutableDictionary
NSKeyValueUndefinedGetter
NSXPCListenerEndpoint
NSKeyValueCollectionGetter
NSStackObservedValue
NSSupportedPronounValidation
NSKeyValueGetter
_NSMetadataQueryResultGroupArray
NSNumberFormatter
_object:trackChangeForKeyOrKeys:operation:
appendTransform:
_debugSignalSource
developmentLocalization
separatorRegex
setClient:
_percentEncodedQuery
bundleURLForExecutableAtURL:
getRelationship:ofDirectoryAt:toItemAt:error:
hasItemConformingToTypeIdentifier:
_reason
initWithKey:value:
operation
performBarrier
whenFinishedPerformProcedure:
_swiftPunctuationCharacters
dateWithEra:year:month:day:hour:minute:second:nanosecond:
prepareUserActivityForLaunchingWithOptions:completionHandler:
setDataDetectorResult:
setLastPresentedItemEventIdentifier:
T@\"_NSPersonNameComponentsStyleFormatterShortVariantGeneral\",R
_mutatingMethods
radians
T@\"NSString\",N,C
initWithRange:replacementString:alternativeStrings:
_getCString:maxLength:encoding:
_key
charactersToBeSkipped
setShortStandaloneQuarterSymbols:
stringsByAppendingPathComponent:
_encodeCString:length:forKey:
copyStringWithMarkdown:formatConfiguration:bundleLocalizations:localization:
initWithTypeIdentifier:dynamicIdentifier:options:
instanceMethodDescriptionForSelector:
micrometers
setContentAttributes:
T@\"<NSCoding>\",R,&
JSONObjectWithData:options:error:
_genericIndex
canSelectUserInflection
objectAtIndexedSubscript:
targetUnitFromKilograms:
_isLink:
outputStreamToBuffer:capacity:
decimalNumberBySubstracting:
physicalMemory
setQueuePriority:
unarchiverDidFinish:
orderedSetByApplyingDifference:
_findFactoriesForPlugInType:
deviceNumbers
removePendingClaims:
setPartOfSpeech:
user
TB,V_shouldEnableMaterializationDuringAccessorBlock
__supportedScriptDefaultsFromScriptName:
_makePresenter:observeChangeWithSubitemURL:
_unitsStyle
executableArchitectures
insertItem:
isEligibleForPrediction
T@\"NSString\",R,V_secureID
_loader
_setShouldRelaunchDueToAutomaticTerminationStateChangedHandler:
valueWithRange:
evaluateWithObject:
expressionValueWithObject:context:
fileSize
initWithFormat:options:locale:arguments:
cubicMillimeters
localizeParsingMarkdown
remove
_tagSchemeForScheme:
_updateFormatterCacheIfNeeded_locked:unitsStyle:
_urlWrapper
predicateWithLeftExpression:rightExpression:customSelector:
usesMetricSystem
decimalNumberByRaisingToPower:
replaceItemAtURL:withItemAtURL:backupItemName:options:resultingItemURL:error:
T@\"NSData\",N,R
_checkForInvalidMutationWithSelector:
_portInvalidated:
setWithObject:
sharedFrameworksPath
bits
transitInformationCheckingResultWithRange:components:
_web_URLByRemovingLastPathComponent_nowarn
logSuspensionWarning
setUnitsStyle:
responseWithError:
initWithDouble:
icuType
familyName
initWithShort:
stringForValue1:unit1:value2:unit2:
reservedSpaceLength
TI,R,V_removedResolveFlags
URLPasswordAllowedCharacterSet
_mutableOrderedSetValueForKeyPath:ofObjectAtIndex:
fileHandleForWriting
inputStreamWithData:
parser:foundCharacters:
showPools
_determineUnitsToFormat:fromMeasurement:
isForPersonMassUse
setCurrencyGroupingSeparator:
_setProcessAssertion:
_web_startupVolumeName_nowarn
_createMutableOrderedSetValueGetterWithContainerClassID:key:
_createOtherValueGetterWithContainerClassID:key:
T@?,C,V_checkInHandler
_locked_clearHandler:forSource:
_operationArgumentKeyPath
hashFunction
initWithMaximumObjectCount:fullPolicy:outputQueue:
setProperty:forKey:
_fullDescription:
_unregisterUserActivityType:dynamicActivityType:
backedByFileProvider
_web_stringByTrimmingWhitespace
_destroyObserverList
initWithDocumentURL:
levelsOfUndo
setPhonetic:
tagsForString:range:unit:scheme:options:orthography:tokenRanges:
indexPath
T@\"NSString\",C,V_lowerCaseCategoryName
T@\"NSNumber\",R
_onqueue_fileProviders
nextElement
_maxCount
_proxiesByPublisherID
binaryOperatorForSelector
removeAllObjectsWithTarget:
squareMegameters
_isFilePackage
_sharedExtensionContextVendor
initFileURLWithPath:isDirectory:relativeToURL:
kilometersPerHour
preferredMIMEType
initWithReciprocalValue:
_subitemObservationsByEventPath
fileManager:shouldLinkItemAtPath:toPath:
indexSet
pendingKVONotificationArray
startRule
_inProcessFileAccessArbiter
valueWithNonretainedObject:
TS,R
_kernelMaterializationInfo
setXPCType:forSelector:argumentIndex:ofReply:
base64EncodedStringWithOptions:
T#,&,N,V_archivedObjectClass
bitwiseAnd:with:
intersectSet
setNetworkServiceType:
_freeBytes
_setByref:
decimalNumberByMultiplyingBy:withBehavior:
performRelinquish
unsignedCharValue
_additionContext
parentIntent
prepareAndBlockOnClaimRelinquishmentForPresentersOfItemAtLocation:orContainedItem:withRelinquishProcedureGetter:
_RHSobserver
_nickname
_willChangeValuesForKeys:
bundleProxyForCurrentProcess
initWithRange:components:underlyingResult:
initWithUUID:name:discardable:
keyPathExpressionForString:
_cache
_localizedStringForKey:value:table:localizations:
_registrarInterface
initWithInsertIndexes:insertedObjects:removeIndexes:removedObjects:additionalChanges:
pendingClaims
strongToStrongObjectsMapTable
era
shortNameFormat
fileOwnerAccountName
range
sortDescriptorWithKey:ascending:comparator:
substringWithRange:
_hasInvokedClaimer
getObjects:count:
rangeOfCharacterFromSet:options:range:
setUsesGroupingSeparator:
_analyzeTokensInWordRange:paragraphRange:
forwardRelinquishmentForWritingClaim:withID:options:purposeID:subitemURL:toPresenter:usingReplySender:
randomn:
_cacheSize
isEqualToNumber:
respondsToSelector:
zero
_locale
TB,G_isAppRefresh
_endpointForInProcessFileCoordinationServer
_rankTable
setWeekdayOrdinal:
URLSession:dataTask:didReceiveData:
_withTaskDictionary:
hostName
scaleBy:
_includesUnit
allowsConstrainedNetworkAccess
launchedTaskWithLaunchPath:arguments:
__swiftParseFileSystemRepresentation:length:into:isDirectory:
performD
removeAllIndexes
coefficient
setPlusSign:
countForObject:
_determinationType
_startReadingFromXPCObject:
decodeValueOfObjCType:at:
setAttributes:ofItemAtPath:error:
setContext:
_enableStrictSecureDecodingMode
_setUsesCharacterDirection:
dataTaskWithRequest:completionHandler:
isCancellable
_makePresenter:observeMoveToURL:withSubitemURL:
_web_localizedDescription
plugInUnregisterFactoryUUID:typeUUID:
reverseTransformedValue:
defaultQueue
extensionPointIdentifier
scheduledTimerWithTimeInterval:target:selector:userInfo:repeats:
__givenNameFirstOrdering
URLWithString:relativeToURL:
_accumulator
_parameterString
_setEligibleForUserActivityHandoff:
fragmentRange
numberOfArguments
_calendar
_isBackup
_publishingHandler
_removeOtherVersionsOfItemAtURL:temporaryStorageIdentifier:error:
_stringFromStringArray:
_web_stringRepresentationForBytes:
encoderCodingPathNode
stringByReplacingPercentEscapesUsingEncoding:
Tq,R,V_columnCount
_handler
_setDefaultTimeZone:
T{_NSRange=QQ},R,V_replacementRangeInResult
floatValue
initWithContentsOfFile:options:maxLength:error:
whenRevokedPerformProcedure:
URLSession:task:willBeginDelayedRequest:completionHandler:
_prepareUserActivityForLaunchingWithOptions:completionHandler:
_writerWithID:didFinishWritingForURL:
squareCentimeters
timeZoneWithName:
_asciiDescription
_options
_singleByte_confidence
milliseconds
T@\"NSPersonNameComponentsFormatter\",R,C,V_masterFormatter
T{_NSRange=QQ},R,V_range
__redoCommonDoSingle:
decodeTopLevelObjectAndReturnError:
initWithValidatedFormat:validFormatSpecifiers:error:
setObjectZone:
shouldFallBack
T@\"NSUnitDuration\",R,C
_expireAllActivities
_initWithValues:
outputStream
variantFittingPresentationWidth:
_numberingSystemForLocaleIdentifier:
dictionaryWithValuesForKeys:
extensionWithURL:completion:
serializeList:
setLevelsOfUndo:
repeats
_additionalInvalidationHandler
initWithPredicateOperator:leftKeyPath:rightKeyPath:
setInterruptionHandler:
terminationHandler
allowEvaluation
_addPort:forMode:
_enumerateChangesInDiffOrderWithBlock:
head
_stringForCalendarUnit:value:
_type
changedURL
next
T@\"NSAttributedString\",R,N
gramsPerLiter
replaceObjectsAtIndexes
setFormatOptions:
expressionBlock
_invalidationHandler
fileType
T@\"NSBundle\",R,&,D,N
_web_changeFileAttributes_nowarn:atPath:
checkCount:
collationIdentifier
indexAtPosition:
lastPresentedItemEventIdentifier
T@\"<NSObject><NSCopying><NSCoding>\",R,C
dataFromRange:documentAttributes:error:
persistentDomainNames
propertyList
unsignedShortValue
decameters
Tq,N,V_definiteness
dataFromPropertyList:format:errorDescription:
initWithKey:ascending:comparator:
setName:
T@\"NSFileHandle\",R,&
subpathsAtPath:
_forwardStackInvocation:
indexOfObjectIdenticalTo:
isRepeatedDay
_endEventGroupingIfOpen
addReacquirer:forPresenterID:
performSelector:object:afterDelay:
subjectForm
_length
_addResult:
_forEachRelevantAccessClaimExcludingClaimsFromSuperarbiter:performProcedure:
_localizedComputerName
_addr
encodeRect:forKey:
removeFileProvider:
_additionObserver
_selectorOrBlock
addKeywordsFromArray:
exemplarCharacterSet
fileURLWithPath:isDirectory:
uniqueIdentifier
TB,R,GisCancelled
sequence
setGroupingAttributes:
__supportedNameDefaultsFromLocalization:
_valueFromFaultDictionary:forKey:
cancelled
precomposedStringWithCompatibilityMapping
removePort:forMode:
stringFromPersonNameComponents:
_undoStack
checkModify
_assertion
_createValuePrimitiveGetterWithContainerClassID:key:
_temporaryMapReplaceObject:withObject:
appendAttributedString:
fileAttributesAtPath:traverseLink:
isGranted
newtonsPerMetersSquared
totalDataWritten
TQ,VprovidedItemRecursiveGenerationCount
loadingPriority
_delayAutomaticTermination:
_hasVM
_newLocaleWithIdentifier:
bundleUserLanguages
paragraphRangeForRange:
_parentUserActivity
dayOfCommonEra
sendMessage:completionHandler:
asyncResolveWithCallbackClient:
__decoderInfoForAllowedClassesWarning
_forgetAccessClaimForID:
addObserver:selector:name:object:
addPublisher:forID:withValues:isOld:
beginActivityWithOptions:reason:
searchList
sendLowDiskSpaceNotification
_cocoaErrorStringWithKind:
decodeXPCObjectOfType:forKey:
passwordRange
veryShortMonthSymbols
_isReservedWordInParser:
objectIsForcedForKey:inDomain:
_helper
_redoStack
_writingRelinquishmentCount
privateFrameworksURL
sharedMappings
_thirdPartyPreferencesDomain
shouldCoerceForCoding
startAccessingSecurityScopedResource
useDaylight
setSet:
URLForPublishingUbiquitousItemAtURL:expirationDate:error:
_allowsExtendedAttributes
_setValue:forKeyPath:ofObjectAtIndex:
containerClassID
dominantLanguage
filePosixPermissions
numberWithUnsignedLongLong:
_accessPresenterInfoUsingBlock:
_writeMonitoringSource
decodeLongForKey:
directoryAttributes
enableUndoRegistration
_checkCount
_decodeError
indexWithOptions:passingTest:
setQuarter:
setStandardUserDefaults:
setStateDescriptor:
valueForAttribute:
_NSItemProviderTypeCoercion_coercedNSDataValueFromNSURLValue:error:
T@\"NSString\",R,C,V_name
_tags
_createValueGetterWithContainerClassID:key:
_web_backgroundRemoveFileAtPath:
orderedSetWithObjects:count:
setAllowsExpensiveNetworkAccess:
setDetermination:
TB,R,G_isBackup
_interface
T@\"NSString\",C,N,V_possessiveAdjectiveForm
distanceFromLocation:
timeZone
T@\"NSDictionary\",C,D,S_setOptions:
_attributedStringWithFormat:options:locale:arguments:
bplistMarker
classForArchiver
_initWithMetadata:
readDataOfLength:buffer:
setProcessManager:
_selfFraction
multiply:by:
pathForResource:ofType:inDirectory:
_possessiveForm
skipSet
T@\"NSString\",C,V_itemIdentifier
becomeCurrent
_replacementKind
pausingHandler
uppercaseStringWithLocale:
_estimatedCount
currentOperation
observeNewProvider:
thematicBreakIntentWithIdentity:nestedInsideIntent:
_contentsURL
_strictlyUnarchivedObjectOfClasses:fromData:error:
_triedConnection
abortParsing
components:fromDateComponents:toDateComponents:options:
fileWrappers
timersForMode:
_web_createFileAtPathWithIntermediateDirectories:contents:attributes:directoryAttributes:
deleteSavedUserActivitiesWithPersistentIdentifiers:completionHandler:
fireDate
validateValue:error:
Tq,N
_url1
index
predicateMatchingIdentifiers:
serializerStream
sortUsingComparator:
T{_NSRange=QQ},R
_cacheGenerationCount
boundedBy:
collapsesLargestUnit
keyPathsForValuesAffectingIsReady
minimumDaysInFirstWeek
_createDispatchData
_createMutableSetValueGetterWithContainerClassID:key:
_secTaskRef
metersPerSecondSquared
_state
fetchUserActivityWithUUID:completionHandler:
loadFileCopyWithOptions:completionHandler:
_localizedAttributedStringWithFormat:options:
_registerFormatter:forErrorKey:parameters:
attemptOptIn:
config
T@\"NSArray\",N,R
_newZStringWithString:
_providedItemAtURL:didLosePresenterWithID:
_web_addErrorsWithCodesAndDescriptions:inDomain:
cancelPerformSelector:target:argument:
isFromConnection:
sizeValue
__old_unswizzled_keyPathsForValuesAffectingValueForKey:
__thaiConsonantSet
_isEligibleForUserActivityHandoff
TB,GisEligibleForPrediction
_numberFormatter
connection:handleInvocation:isReply:
setCookiePartitionIdentifier:
setNegativePrefix:
stringVersion
registerUndoWithTarget:selector:object:
_addFileProvider:
fahrenheit
propertyListWithStream:options:format:error:
unlock
_adoptChildUserInfo
percentEncodedQueryItems
_parent
outputStreamWithURL:append:
partialFolderMaterializationInfoWithOperation:fileName:
UTF8String
_setEncodedHost:
_willChange
arrayByAddingObject:
T@\"NSMorphology\",R,C,V_dependentMorphology
_preferredLanguages
_writeRelinquishmentsByPresenterID
dataWithContentsOfURL:options:maxLength:error:
parserDidEndDocument:
writeToURL:atomically:encoding:error:
_keyLen
publish
outputStreamToFileAtPath:append:
ceiling:
initWithURL:includingPropertiesForKeys:options:errorHandler:
set_ignoresFallbacks:
decodeObjectForKey:error:
regularFileContents
tibetanInitialsCreator
max
pid
_claim
_modificationDate
isPartialStringValid:proposedSelectedRange:originalString:originalSelectedRange:errorDescription:
_rollbackUndoGrouping
initWithRange:phoneNumber:
pinTags:inBundle:priority:completionHandler:
setCancellationHandler:
setValidated:
URLForResource:withExtension:subdirectory:inBundleWithURL:
_processAssertion
addObserverForName:object:suspensionBehavior:queue:usingBlock:
archiverWillFinish:
copy
length
setTemporaryResourceValue:forKey:
mainDocumentURL
_scriptNameForScriptIndex:
broadcast
getArgumentTypeAtIndex:
milliamperes
options
URLSession:dataTask:didBecomeStreamTask:
_deprecated_scanUpToCharactersFromSet:intoString:
_referentConcept
_treatNilValuesLikeEmptyOrderedSets
grammarDetails
localizeWithOptions:
Tq
_remoteObjectInterfaceClass
dateFromComponents:
isAncestorOfObject:
openURL:completion:
PID
T@\"NSMorphology\",R
_setThirdPartyApplicationsCanAccessUserInflection:
isEqualToAttributedString:
symbolicLinkDestinationURL
assumesHTTP3Capable
performActivityWithOptions:reason:block:
_replacementsFromMetadataArray:
_cfBundleIfPresent
completeRequestReturningItems:
sortedArrayUsingSelector:
T@\"NSSet\",C,V_observedUbiquityAttributes
_generationCount
_mainThreadPerformRemoteUndoForUUID:isRedo:withReply:
mutableSet
setFileURL:
_withExtrapolatedPronouns
_discardable
createSymbolicLinkAtPath:withDestinationPath:error:
forwardReacquisitionForWritingClaim:withID:toPresenterForID:usingReplySender:
urlsFor:in:
_NSItemProviderTypeCoercion_coercedNSFileWrapperValueFromNSDataValue:error:
addObservationTransformer:
localizedStringForKey:value:table:localization:
operationDescription
_adaptive
setCountLimit:
yottabits
_objects
isNSValue__
T@\"NSObject\",R,&
enumeratorWithMapTable:
seekToFileOffset:
setFilename:
setNotificationBatchingInterval:
setPredicateOperator:
addVersionOfItemAtURL:withContentsOfURL:options:error:
overcommitsOperations
petabits
sendPort
setDelegate:
_removalObservanceIndex
_currentGlobalUserInflectionIfAvailable
_fastIterator
_localizedStringNoCacheNoMarkdownParsingForKey:value:table:bundleLocalizations:localization:formatSpecifierConfiguration:
_readBytesFromPath:maxLength:bytes:length:didMap:options:reportProgress:error:
indexInRange:options:passingTest:
_isDeallocating
_addObserver:selector:name:object:options:
_saxHandler
actorQueueManagerLock
refCount
_allowDecodingCyclesInSecureMode
readFromURL:options:error:
setEraSymbols:
setFetchingVersionsDoneBlock:
addValue:forHTTPHeaderField:
Tq,R,V_indentationLevel
_changeType
_enumerateDatesStartingAfterDate:matchingComponents:options:usingBlock:
abs:
setUsesMainThreadDuringReliquishing:
setWithArray:
valueForHTTPHeaderField:
_customSubclass
_wakeup
member:
_purposeIdentifierLockedDown
_resetQueryState
handleErrorsWithBlock:
initWithInflectionRule:
keyPathsForValuesAffectingIsFinished
setFinished:
TB,R,V_requiresProviding
count
dateByAddingComponents:toDate:options:
_readContentsFromURL:path:itemKind:options:error:
_subpredicate
addObserver:
date
initWithSpecifier:symbol:converter:
getObjects:range:
_fileProviderInterface
_validateInvocationContext
localizedStringForCollatorIdentifier:
TB,GisSuspended
completionWithBlock:
initWithQueue:auditToken:
macCatalystApp
mapTableWithStrongToStrongObjects
__copySwiftEncodedQuery:encoding:
_alternativesForInputString:
frameLength
setIncludesCount:
_currentUniqueIdentifier
_setEmitsChanges:
extraArgumentCount
isMemoryPressureSensitive
setCalendarFormat:
_fastByteContents
_fileHandlesForEvictionProtection
_isInvalid
localizedAttributedStringWithFormat:options:
percentEncodedPath
T@\"NSString\",C,N,V_subjectForm
_expressionWithSubstitutionVariables:
decodeDictionaryWithKeysOfClasses:objectsOfClasses:forKey:
fractionCompleted
initWithAlgorithm:operation:dataHandler:
internalWritePath:errorHandler:remapContents:hardLinkPath:
setArgument:atIndex:
setCalendar:
_memoryPressureSensitive
classNameForClass:
componentsWithURL:resolvingAgainstBaseURL:
cubicMiles
forEachExistingComponentWithComponents:performBlock:
initWithContentsOfURL:
initWithReceivePort:sendPort:components:
invocation
__redoSingle
cancel
collection
imperialTeaspoons
languagesForScript:
taskState
_writerWithPurposeID:didMoveItemAtURL:toURL:withFSID:andFileID:
forEachReactorToItemOrContainedItemPerformProcedure:
primaryPresentedItemURL
Tq,V_numberOfInvitations
_cTypeString
archivedObjectClass
attributeNames
initWithUnsignedLong:
setWebpageURL:
_nonLocalVersion
dateWithCalendarFormat:timeZone:
isUndoRegistrationEnabled
setNamePrefix:
_eligibleForUserActivityReminders
_timeZoneWithAbbreviation:
parseData:
processManager
removeObserver:fromObjectsAtIndexes:forKeyPath:
debugDescription
ensureProvidersOfItemsAtReadingLocations:writingLocations:thenContinue:
julianCutoverDay
milesPerGallon
mutableAttributedString
setPercentEncodedPassword:
setStandardError:
setVerbForm:
searchItems
T@\"NSDecimalNumber\",R,C
_fixedUpSideFaultError:
_setAutomaticFileProviderReregistrationDisabled:
_idleQueue
_rangeArray
_typeOrder
intersectHashTable:
size
T@\"NSNotificationCenter\",R
_dataHandler
_group
_requestFinishedGroup
addConstraintsTo:
initWithDataNoCopy:
object:didRemoveObservance:recurse:
_acceptExpressions:flags:
_invokeUnpublishingHandler
copyWithData:urlWrapper:cleanupHandler:error:
decodeObject
getParagraphStart:end:contentsEnd:forRange:
setAllowsPersistentDNS:
appendString:with:
replacementTable
totalAutoreleasedObjects
_affectingProperties
pointerArrayWithPointerFunctions:
_swiftURLPasswordAllowedCharacterSet
relinquishmentForWrite:toPresenterForID:
setDescriptionFunction:
Tq,V_determinationType
_index
newWithPath:prepend:attributes:cross:depth:
TB,V_inSubarbiter
.cxx_destruct
_movingItemAtURL:withInfo:completionHandler:
deserializeNewKeyString
getFormatter
initWithMorphology:
alternateQuotationEndDelimiter
average:
startDate
observableWithName:object:
readToEndOfFileInBackgroundAndNotify
setLongLong:forKey:
T@\"NSPredicate\",C,N,V_predicate
_rangeCount
target
getItem:
kSecondsInMinute
_allocWithExtraBytes:
decodePropertyListForKey:
```
