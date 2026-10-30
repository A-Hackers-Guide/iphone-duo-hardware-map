# `_UIVisualEffectFilterEntry`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIVisualEffectDiffable`
- 9 instance variables, 13 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"CAFilter" _filter;
B _useRelaxedDiffingRule;
@"NSString" _filterType;
@"NSDictionary" _configurationValues;
@"NSDictionary" _requestedValues;
@"NSDictionary" _identityValues;
d _requestedScaleHint;
d _identityScaleHint;
@"NSString" _filterName;
```

## Properties

```
@property (T@"NSString",C,N,V_filterType) filterType;
@property (T@"NSDictionary",C,N,V_configurationValues) configurationValues;
@property (T@"NSDictionary",C,N,V_requestedValues) requestedValues;
@property (T@"NSDictionary",C,N,V_identityValues) identityValues;
@property (Td,N,V_requestedScaleHint) requestedScaleHint;
@property (Td,N,V_identityScaleHint) identityScaleHint;
@property (TB,N,V_useRelaxedDiffingRule) useRelaxedDiffingRule;
@property (T@"CAFilter",R,N) filter;
@property (T@"NSString",R,C,N,V_filterName) filterName;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIVisualEffectFilterEntry setConfigurationValues:];
-[_UIVisualEffectFilterEntry filter];
-[_UIVisualEffectFilterEntry filterName];
-[_UIVisualEffectFilterEntry requestedValues];
-[_UIVisualEffectFilterEntry identityValues];
-[_UIVisualEffectFilterEntry convertToIdentity];
-[_UIVisualEffectFilterEntry configurationValues];
-[_UIVisualEffectFilterEntry identityScaleHint];
-[_UIVisualEffectFilterEntry setUseRelaxedDiffingRule:];
-[_UIVisualEffectFilterEntry requestedScaleHint];
-[_UIVisualEffectFilterEntry filterType];
-[_UIVisualEffectFilterEntry setRequestedScaleHint:];
-[_UIVisualEffectFilterEntry useRelaxedDiffingRule];
-[_UIVisualEffectFilterEntry copyForTransitionOut];
-[_UIVisualEffectFilterEntry setIdentityScaleHint:];
-[_UIVisualEffectFilterEntry setRequestedValues:];
-[_UIVisualEffectFilterEntry scaleHintAsRequested:];
-[_UIVisualEffectFilterEntry setIdentityValues:];
-[_UIVisualEffectFilterEntry copyForTransitionToEffect:];
-[_UIVisualEffectFilterEntry description];
-[_UIVisualEffectFilterEntry initWithFilterType:configurationValues:requestedValues:identityValues:];
-[_UIVisualEffectFilterEntry canTransitionToEffect:];
-[_UIVisualEffectFilterEntry forceUniqueName];
-[_UIVisualEffectFilterEntry copyWithZone:];
-[_UIVisualEffectFilterEntry setFilterType:];
-[_UIVisualEffectFilterEntry isSameTypeOfEffect:];
-[_UIVisualEffectFilterEntry valueAsRequested:];
```
