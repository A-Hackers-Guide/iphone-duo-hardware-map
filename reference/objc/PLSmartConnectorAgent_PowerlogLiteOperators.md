# `PLSmartConnectorAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 10 instance variables, 10 properties, 27 instance methods, 5 class methods

## Instance variables

```
@"PLIOKitOperatorComposition" _iokitOrion;
@"PLTimer" _timer;
@"NSNumber" _preStatus;
@"NSNumber" _curStatus;
@"NSString" _preName;
@"NSString" _curName;
@"NSString" _preModel;
@"NSString" _curModel;
@"NSData" _preVersion;
@"NSData" _curVersion;
```

## Properties

```
@property (T@"PLIOKitOperatorComposition",R,V_iokitOrion) iokitOrion;
@property (T@"PLTimer",&,V_timer) timer;
@property (T@"NSNumber",&,V_preStatus) preStatus;
@property (T@"NSNumber",&,V_curStatus) curStatus;
@property (T@"NSString",&,V_preName) preName;
@property (T@"NSString",&,V_curName) curName;
@property (T@"NSString",&,V_preModel) preModel;
@property (T@"NSString",&,V_curModel) curModel;
@property (T@"NSData",&,V_preVersion) preVersion;
@property (T@"NSData",&,V_curVersion) curVersion;
```

## Class methods

```
+[PLSmartConnectorAgent entryEventForwardDefinitions];
+[PLSmartConnectorAgent load];
+[PLSmartConnectorAgent isEnabled];
+[PLSmartConnectorAgent entryEventForwardDefinitionEAStatus];
+[PLSmartConnectorAgent entryEventForwardDefinitionStatus];
```

## Instance methods

```
-[PLSmartConnectorAgent setTimer:];
-[PLSmartConnectorAgent init];
-[PLSmartConnectorAgent timer];
-[PLSmartConnectorAgent initOperatorDependancies];
-[PLSmartConnectorAgent log];
-[PLSmartConnectorAgent reArmCallback];
-[PLSmartConnectorAgent curName];
-[PLSmartConnectorAgent preName];
-[PLSmartConnectorAgent curModel];
-[PLSmartConnectorAgent curStatus];
-[PLSmartConnectorAgent curVersion];
-[PLSmartConnectorAgent externalAccessoryConnected:];
-[PLSmartConnectorAgent externalAccessoryDisconnected:];
-[PLSmartConnectorAgent iokitOrion];
-[PLSmartConnectorAgent logEventForwardEAAccessory:];
-[PLSmartConnectorAgent logEventForwardStatus:withName:withModel:andVersionInfo:];
-[PLSmartConnectorAgent preModel];
-[PLSmartConnectorAgent preStatus];
-[PLSmartConnectorAgent preVersion];
-[PLSmartConnectorAgent setCurModel:];
-[PLSmartConnectorAgent setCurName:];
-[PLSmartConnectorAgent setCurStatus:];
-[PLSmartConnectorAgent setCurVersion:];
-[PLSmartConnectorAgent setPreModel:];
-[PLSmartConnectorAgent setPreName:];
-[PLSmartConnectorAgent setPreStatus:];
-[PLSmartConnectorAgent setPreVersion:];
```
