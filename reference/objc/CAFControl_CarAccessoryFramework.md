# `CAFControl`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAFCacheableDescription`, `CAFEntity`, `NSCopying`
- 23 instance variables, 37 properties, 79 instance methods, 4 class methods

## Instance variables

```
B _hasErrorState;
B _isDisabled;
B _isRestricted;
B _isHidden;
B _hasResponse;
B _isNotificationEnabled;
B _shouldInitialize;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _valueLock;
@"CAFService" _service;
@"NSArray" _requestParameters;
@"NSArray" _responseParameters;
@"NSNumber" _instanceID;
@"NSNumber" _errorInstanceID;
@"NSNumber" _disabledInstanceID;
@"NSNumber" _restrictedInstanceID;
@"NSNumber" _hiddenInstanceID;
@"NSString" _controlType;
@"NSUUID" _uniqueIdentifier;
@"NSString" _typeName;
@"NSNumber" _priority;
Q _sender;
@"CARObserverHashTable" _observers;
@"CAFCachedDescription" _cachedDescription;
```

## Properties

```
@property (T@"NSNumber",R,N,V_instanceID) instanceID;
@property (T@"NSNumber",R,N,V_errorInstanceID) errorInstanceID;
@property (T@"NSNumber",R,N,V_disabledInstanceID) disabledInstanceID;
@property (T@"NSNumber",R,N,V_restrictedInstanceID) restrictedInstanceID;
@property (T@"NSNumber",R,N,V_hiddenInstanceID) hiddenInstanceID;
@property (T@"NSString",R,N,V_controlType) controlType;
@property (T@"NSUUID",&,N,V_uniqueIdentifier) uniqueIdentifier;
@property (T@"NSString",&,N,V_typeName) typeName;
@property (TB,N,V_hasErrorState) hasErrorState;
@property (TB,N,V_isDisabled) isDisabled;
@property (TB,N,V_isRestricted) isRestricted;
@property (TB,N,V_isHidden) isHidden;
@property (T@"NSNumber",R,N,V_priority) priority;
@property (TQ,N,V_sender) sender;
@property (TB,N,V_isNotificationEnabled) isNotificationEnabled;
@property (TB,R,N,V_shouldInitialize) shouldInitialize;
@property (T@"CARObserverHashTable",&,N,V_observers) observers;
@property (T@"CAFCachedDescription",&,N,V_cachedDescription) cachedDescription;
@property (T{os_unfair_lock_s=I},N,V_valueLock) valueLock;
@property (T@"CAFCar",R,W,N) car;
@property (T@"CAFAccessory",R,W,N) accessory;
@property (T@"CAFService",R,W,N,V_service) service;
@property (T@"NSString",R,N) fullDescription;
@property (TB,R,N) outgoing;
@property (TB,R,N) incoming;
@property (TB,R,N,V_hasResponse) hasResponse;
@property (TB,R,N) notifies;
@property (T@"NSArray",R,N,V_requestParameters) requestParameters;
@property (T@"NSArray",R,N,V_responseParameters) responseParameters;
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
+[CAFControl controlIdentifier];
+[CAFControl _appendParametersDescription:parameters:];
+[CAFControl controlWithService:config:];
+[CAFControl observerProtocol];
```

## Instance methods

```
-[CAFControl isRestricted];
-[CAFControl requestParameters];
-[CAFControl setIsHidden:];
-[CAFControl priority];
-[CAFControl hasResponse];
-[CAFControl cachedDescription];
-[CAFControl typeName];
-[CAFControl removeObserver:];
-[CAFControl compare:];
-[CAFControl dealloc];
-[CAFControl setUniqueIdentifier:];
-[CAFControl fullDescription];
-[CAFControl uniqueIdentifier];
-[CAFControl isDisabled];
-[CAFControl addObserver:];
-[CAFControl invalidate];
-[CAFControl sender];
-[CAFControl isHidden];
-[CAFControl isNotificationEnabled];
-[CAFControl service];
-[CAFControl controlType];
-[CAFControl instanceID];
-[CAFControl setCachedDescription:];
-[CAFControl setIsDisabled:];
-[CAFControl hash];
-[CAFControl setIsRestricted:];
-[CAFControl description];
-[CAFControl setObservers:];
-[CAFControl setSender:];
-[CAFControl observers];
-[CAFControl registerObserver:];
-[CAFControl copyWithZone:];
-[CAFControl isEqual:];
-[CAFControl name];
-[CAFControl unregisterObserver:];
-[CAFControl accessory];
-[CAFControl setTypeName:];
-[CAFControl outgoing];
-[CAFControl car];
-[CAFControl responseParameters];
-[CAFControl incoming];
-[CAFControl propertiesDescription];
-[CAFControl setIsNotificationEnabled:];
-[CAFControl usable];
-[CAFControl errorInstanceID];
-[CAFControl readInstanceIDs];
-[CAFControl supportsDisable];
-[CAFControl _didNotifyWithValue:];
-[CAFControl _didRequestWithValue:response:];
-[CAFControl _didUpdate];
-[CAFControl allInstanceIDs];
-[CAFControl baseCAFClass];
-[CAFControl comparisonKeys];
-[CAFControl currentDescriptionForCache:];
-[CAFControl disabledInstanceID];
-[CAFControl handleNotificationWithValue:];
-[CAFControl handleRegistrationWithInstanceID:registered:];
-[CAFControl handleRegistrationWithInstanceID:value:registered:];
-[CAFControl handleRequestWithValue:withResponse:];
-[CAFControl handleUpdateWithInstanceID:value:];
-[CAFControl handleValueAndError:value:];
-[CAFControl hasErrorState];
-[CAFControl hiddenInstanceID];
-[CAFControl initWithService:config:];
-[CAFControl notifies];
-[CAFControl notifyWithValue:];
-[CAFControl parametersDescription];
-[CAFControl pluginID];
-[CAFControl registrationInstanceIDs];
-[CAFControl requestWithValue:response:];
-[CAFControl restrictedInstanceID];
-[CAFControl setHasErrorState:];
-[CAFControl setValueLock:];
-[CAFControl shouldInitialize];
-[CAFControl supportsError];
-[CAFControl supportsHidden];
-[CAFControl supportsRestricted];
-[CAFControl supportsStates];
-[CAFControl valueLock];
```
