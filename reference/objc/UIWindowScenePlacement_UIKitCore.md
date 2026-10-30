# `UIWindowScenePlacement`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDebugDescriptionProviding`, `NSCopying`
- 0 instance variables, 8 properties, 15 instance methods, 2 class methods

## Properties

```
@property (TB,R,N) _preserveLayout;
@property (TB,R,N) _requestFullscreen;
@property (TB,R,N) _requestCenterSlot;
@property (TB,R,N) _requestBackground;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIWindowScenePlacement _default];
+[UIWindowScenePlacement _placementType];
```

## Instance methods

```
-[UIWindowScenePlacement debugDescription];
-[UIWindowScenePlacement succinctDescriptionBuilder];
-[UIWindowScenePlacement descriptionWithMultilinePrefix:];
-[UIWindowScenePlacement _init];
-[UIWindowScenePlacement succinctDescription];
-[UIWindowScenePlacement debugDescriptionWithMultilinePrefix:];
-[UIWindowScenePlacement description];
-[UIWindowScenePlacement copyWithZone:];
-[UIWindowScenePlacement isEqual:];
-[UIWindowScenePlacement descriptionBuilderWithMultilinePrefix:];
-[UIWindowScenePlacement _preserveLayout];
-[UIWindowScenePlacement _createConfigurationWithError:];
-[UIWindowScenePlacement _requestBackground];
-[UIWindowScenePlacement _requestCenterSlot];
-[UIWindowScenePlacement _requestFullscreen];
```
