# `CAFCharacteristic`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAFCacheableDescription`, `CAFEntity`, `NSCopying`
- 36 instance variables, 58 properties, 120 instance methods, 5 class methods

## Instance variables

```
B _hasErrorState;
B _isDisabled;
B _isRestricted;
B _isHidden;
B _writable;
B _isMutable;
B _hasInitialValue;
B _hasLargePayload;
B _supportsInvalid;
B _isNotificationEnabled;
B _shouldInitialize;
B _initializationFinished;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _valueLock;
@"NSError" _error;
@"CAFService" _service;
@"NSNumber" _instanceID;
@"NSNumber" _errorInstanceID;
@"NSNumber" _disabledInstanceID;
@"NSNumber" _notifierInstanceID;
@"NSNumber" _restrictedInstanceID;
@"NSNumber" _hiddenInstanceID;
@"NSString" _characteristicType;
@"NSUUID" _uniqueIdentifier;
@"NSString" _typeName;
@"CAFCharacteristicValue" _characteristicValue;
@"NSNumber" _notifierValue;
@"CAFCharacteristicMetadata" _metaData;
@"NSNumber" _priority;
@"CARObserverHashTable" _observers;
@"CAFCachedDescription" _cachedDescription;
Q _lastState;
@ _cachedValue;
@ _pendingValue;
Q _lockState;
Q _transactionId;
@"NSObject<OS_dispatch_source>" _echoSuppressionTimer;
```

## Properties

```
@property (T@"NSNumber",R,N,V_instanceID) instanceID;
@property (T@"NSNumber",R,N,V_errorInstanceID) errorInstanceID;
@property (T@"NSNumber",R,N,V_disabledInstanceID) disabledInstanceID;
@property (T@"NSNumber",R,N,V_notifierInstanceID) notifierInstanceID;
@property (T@"NSNumber",R,N,V_restrictedInstanceID) restrictedInstanceID;
@property (T@"NSNumber",R,N,V_hiddenInstanceID) hiddenInstanceID;
@property (T@"NSString",R,N,V_characteristicType) characteristicType;
@property (T@"NSUUID",&,N,V_uniqueIdentifier) uniqueIdentifier;
@property (T@"NSString",&,N,V_typeName) typeName;
@property (T@"CAFCharacteristicValue",&,N,V_characteristicValue) characteristicValue;
@property (T@"NSNumber",&,N,V_notifierValue) notifierValue;
@property (TB,N,V_hasErrorState) hasErrorState;
@property (TB,N,V_isDisabled) isDisabled;
@property (TB,N,V_isRestricted) isRestricted;
@property (TB,N,V_isHidden) isHidden;
@property (T@"CAFCharacteristicMetadata",R,N,V_metaData) metaData;
@property (TB,R,N,V_isMutable) isMutable;
@property (T@"NSNumber",R,N,V_priority) priority;
@property (TB,R,N,V_hasInitialValue) hasInitialValue;
@property (TB,R,N,V_hasLargePayload) hasLargePayload;
@property (TB,R,N,V_supportsInvalid) supportsInvalid;
@property (TB,N,V_isNotificationEnabled) isNotificationEnabled;
@property (TB,R,N,V_shouldInitialize) shouldInitialize;
@property (T@"CARObserverHashTable",&,N,V_observers) observers;
@property (T@"CAFCachedDescription",&,N,V_cachedDescription) cachedDescription;
@property (TB,N,V_initializationFinished) initializationFinished;
@property (TQ,N,V_lastState) lastState;
@property (T{os_unfair_lock_s=I},N,V_valueLock) valueLock;
@property (T@,&,N,V_cachedValue) cachedValue;
@property (T@,&,N,V_pendingValue) pendingValue;
@property (TQ,N,V_lockState) lockState;
@property (TQ,N,V_transactionId) transactionId;
@property (T@"NSError",&,N,V_error) error;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_echoSuppressionTimer) echoSuppressionTimer;
@property (T@"CAFCar",R,W,N) car;
@property (T@"CAFAccessory",R,W,N) accessory;
@property (T@"CAFService",R,W,N,V_service) service;
@property (T@"NSString",R,N) fullDescription;
@property (T@,&,N) value;
@property (T@"NSString",R,N) formattedValue;
@property (TB,R,N) hasError;
@property (TQ,R,N) state;
@property (TB,R,N,GisCurrent) current;
@property (TB,R,N,GisInitializing) initializing;
@property (TB,R,N) isInvalid;
@property (T@"NSString",R,N) format;
@property (T@"NSString",R,N) baseFormat;
@property (TB,R,N) notifies;
@property (TB,R,N) readable;
@property (TB,R,N,V_writable) writable;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,N) name;
@property (TB,R,N) usable;
@property (T#,R,N) baseCAFClass;
@property (T@"NSArray",R,N) comparisonKeys;
```

## Class methods

```
+[CAFCharacteristic characteristicFormats];
+[CAFCharacteristic characteristicWithService:config:];
+[CAFCharacteristic observerProtocol];
+[CAFCharacteristic primaryCharacteristicFormat];
+[CAFCharacteristic secondaryCharacteristicFormats];
```

## Instance methods

```
-[CAFCharacteristic isInitializing];
-[CAFCharacteristic isRestricted];
-[CAFCharacteristic setIsHidden:];
-[CAFCharacteristic characteristicType];
-[CAFCharacteristic priority];
-[CAFCharacteristic setCachedValue:];
-[CAFCharacteristic cachedDescription];
-[CAFCharacteristic setError:];
-[CAFCharacteristic lockState];
-[CAFCharacteristic setLockState:];
-[CAFCharacteristic typeName];
-[CAFCharacteristic metaData];
-[CAFCharacteristic removeObserver:];
-[CAFCharacteristic compare:];
-[CAFCharacteristic formattedValue];
-[CAFCharacteristic dealloc];
-[CAFCharacteristic value];
-[CAFCharacteristic setUniqueIdentifier:];
-[CAFCharacteristic fullDescription];
-[CAFCharacteristic cachedValue];
-[CAFCharacteristic uniqueIdentifier];
-[CAFCharacteristic isMutable];
-[CAFCharacteristic error];
-[CAFCharacteristic isDisabled];
-[CAFCharacteristic addObserver:];
-[CAFCharacteristic invalidate];
-[CAFCharacteristic isHidden];
-[CAFCharacteristic setValue:];
-[CAFCharacteristic isNotificationEnabled];
-[CAFCharacteristic isCurrent];
-[CAFCharacteristic service];
-[CAFCharacteristic instanceID];
-[CAFCharacteristic setCachedDescription:];
-[CAFCharacteristic setIsDisabled:];
-[CAFCharacteristic hash];
-[CAFCharacteristic setIsRestricted:];
-[CAFCharacteristic writable];
-[CAFCharacteristic description];
-[CAFCharacteristic setObservers:];
-[CAFCharacteristic isInvalid];
-[CAFCharacteristic observers];
-[CAFCharacteristic registerObserver:];
-[CAFCharacteristic copyWithZone:];
-[CAFCharacteristic isEqual:];
-[CAFCharacteristic format];
-[CAFCharacteristic name];
-[CAFCharacteristic unregisterObserver:];
-[CAFCharacteristic accessory];
-[CAFCharacteristic hasError];
-[CAFCharacteristic state];
-[CAFCharacteristic lastState];
-[CAFCharacteristic setLastState:];
-[CAFCharacteristic setTypeName:];
-[CAFCharacteristic car];
-[CAFCharacteristic setTransactionId:];
-[CAFCharacteristic transactionId];
-[CAFCharacteristic _updateStateIfNeeded];
-[CAFCharacteristic propertiesDescription];
-[CAFCharacteristic pendingValue];
-[CAFCharacteristic setPendingValue:];
-[CAFCharacteristic setIsNotificationEnabled:];
-[CAFCharacteristic usable];
-[CAFCharacteristic _lock_setError:];
-[CAFCharacteristic errorInstanceID];
-[CAFCharacteristic hasInitialValue];
-[CAFCharacteristic hasLargePayload];
-[CAFCharacteristic readInstanceIDs];
-[CAFCharacteristic supportsInvalid];
-[CAFCharacteristic supportsDisable];
-[CAFCharacteristic _cancelEchoSuppressionTimer];
-[CAFCharacteristic _didUpdateFromGroupUpdate:];
-[CAFCharacteristic _echoSuppressionTimerFired];
-[CAFCharacteristic _readValueCompletionTransactionID:error:];
-[CAFCharacteristic _resetEchoSuppressionTimer];
-[CAFCharacteristic allInstanceIDs];
-[CAFCharacteristic baseCAFClass];
-[CAFCharacteristic baseFormat];
-[CAFCharacteristic characteristicValue];
-[CAFCharacteristic comparisonKeys];
-[CAFCharacteristic currentDescriptionForCache:];
-[CAFCharacteristic decodeValue:error:];
-[CAFCharacteristic descriptionExtras];
-[CAFCharacteristic disabledInstanceID];
-[CAFCharacteristic echoSuppressionTimer];
-[CAFCharacteristic encodeValue:error:];
-[CAFCharacteristic groupInitializationRequested];
-[CAFCharacteristic handleError:value:];
-[CAFCharacteristic handleRead:value:];
-[CAFCharacteristic handleRegistrationWithInstanceID:registered:];
-[CAFCharacteristic handleRegistrationWithInstanceID:value:registered:];
-[CAFCharacteristic handleUpdateWithInstanceID:value:];
-[CAFCharacteristic handleValueAndError:value:];
-[CAFCharacteristic handleWrite:value:];
-[CAFCharacteristic hasErrorState];
-[CAFCharacteristic hiddenInstanceID];
-[CAFCharacteristic initWithService:config:];
-[CAFCharacteristic initializationFinished];
-[CAFCharacteristic notifierInstanceID];
-[CAFCharacteristic notifierValue];
-[CAFCharacteristic notifies];
-[CAFCharacteristic pluginID];
-[CAFCharacteristic readable];
-[CAFCharacteristic registrationInstanceIDs];
-[CAFCharacteristic restrictedInstanceID];
-[CAFCharacteristic setCachedValueIfAvailableForGroupUpdate:];
-[CAFCharacteristic setCharacteristicValue:];
-[CAFCharacteristic setEchoSuppressionTimer:];
-[CAFCharacteristic setHasErrorState:];
-[CAFCharacteristic setInitializationFinished:];
-[CAFCharacteristic setNotifierValue:];
-[CAFCharacteristic setValueLock:];
-[CAFCharacteristic shouldDeferInitialization];
-[CAFCharacteristic shouldInitialize];
-[CAFCharacteristic supportsError];
-[CAFCharacteristic supportsHidden];
-[CAFCharacteristic supportsNotifier];
-[CAFCharacteristic supportsRestricted];
-[CAFCharacteristic supportsStates];
-[CAFCharacteristic updateValueRequiringRead:];
-[CAFCharacteristic valueLock];
```
