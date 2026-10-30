# `CFXFilterEffectContentDataSource`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `JFXFilterEffectContentDataSource`
- 11 instance variables, 15 properties, 23 instance methods, 0 class methods

## Instance variables

```
B _isContentAvailable;
B _isContentNew;
B _isStyleTransfer;
Q _contentAvailability;
@"NSString" _contentVersion;
@"NSString" _localizedDisplayName;
@"NSString" _localizedAccessibilityName;
@"NSNumber" _requiredProVideoVersion;
@"NSNumber" _isExpensive;
@"NSNumber" _proxyRenderScale;
q _inverseToneMapOperator;
```

## Properties

```
@property (TB,N,V_isContentAvailable) isContentAvailable;
@property (TQ,N,V_contentAvailability) contentAvailability;
@property (T@"NSString",&,N,V_contentVersion) contentVersion;
@property (T@"NSString",&,N,V_localizedDisplayName) localizedDisplayName;
@property (T@"NSString",&,N,V_localizedAccessibilityName) localizedAccessibilityName;
@property (T@"NSNumber",&,N,V_requiredProVideoVersion) requiredProVideoVersion;
@property (TB,N,V_isContentNew) isContentNew;
@property (T@"NSNumber",&,N,V_isExpensive) isExpensive;
@property (TB,N,V_isStyleTransfer) isStyleTransfer;
@property (T@"NSNumber",&,N,V_proxyRenderScale) proxyRenderScale;
@property (Tq,N,V_inverseToneMapOperator) inverseToneMapOperator;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CFXFilterEffectContentDataSource isExpensive];
-[CFXFilterEffectContentDataSource contentVersion];
-[CFXFilterEffectContentDataSource setContentVersion:];
-[CFXFilterEffectContentDataSource localizedDisplayName];
-[CFXFilterEffectContentDataSource setLocalizedDisplayName:];
-[CFXFilterEffectContentDataSource setIsExpensive:];
-[CFXFilterEffectContentDataSource isContentAvailable];
-[CFXFilterEffectContentDataSource isStyleTransfer];
-[CFXFilterEffectContentDataSource contentAvailability];
-[CFXFilterEffectContentDataSource initWithEffectID:];
-[CFXFilterEffectContentDataSource inverseToneMapOperator];
-[CFXFilterEffectContentDataSource isContentNew];
-[CFXFilterEffectContentDataSource localizedAccessibilityName];
-[CFXFilterEffectContentDataSource proxyRenderScale];
-[CFXFilterEffectContentDataSource requiredProVideoVersion];
-[CFXFilterEffectContentDataSource setContentAvailability:];
-[CFXFilterEffectContentDataSource setInverseToneMapOperator:];
-[CFXFilterEffectContentDataSource setIsContentAvailable:];
-[CFXFilterEffectContentDataSource setIsContentNew:];
-[CFXFilterEffectContentDataSource setIsStyleTransfer:];
-[CFXFilterEffectContentDataSource setLocalizedAccessibilityName:];
-[CFXFilterEffectContentDataSource setProxyRenderScale:];
-[CFXFilterEffectContentDataSource setRequiredProVideoVersion:];
```
