# `CBCEModule`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBModule`
- Protocols: `CBContainerModuleProtocol`
- 13 instance variables, 6 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _alsEvents;
@"NSMutableDictionary" _currentInputDict;
@"NSMutableDictionary" _currentOutputDict;
@ _model;
@ _overriddenInput;
@ _currentInput;
B _overriding;
B _use35FeatureInput;
@"NSDictionary" _cachedResult;
d _lastInferenceTime;
d _cadenceSeconds;
# _modelClass;
# _modelInputClass;
```

## Properties

```
@property (T#,V_modelClass) modelClass;
@property (T#,V_modelInputClass) modelInputClass;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CBCEModule copyPropertyForKey:];
-[CBCEModule setProperty:forKey:];
-[CBCEModule stop];
-[CBCEModule dealloc];
-[CBCEModule start];
-[CBCEModule sendNotificationForKey:withValue:];
-[CBCEModule handleNotificationForKey:withProperty:];
-[CBCEModule copyPropertyForKey:withParameter:];
-[CBCEModule modelClass];
-[CBCEModule setModelClass:];
-[CBCEModule modelInputClass];
-[CBCEModule _paramsFromAlsEvent:];
-[CBCEModule copyCachedInferenceForEvent:];
-[CBCEModule copyInference:];
-[CBCEModule copyInferenceForEvent:];
-[CBCEModule initWithQueue:ceModelID:];
-[CBCEModule invalidateInferenceCache];
-[CBCEModule setModelInputClass:];
-[CBCEModule setModelInputWithAlsEvent:ceInput:];
-[CBCEModule setModelInputWithParameters:];
-[CBCEModule shouldRunInferenceAtTime:];
```
