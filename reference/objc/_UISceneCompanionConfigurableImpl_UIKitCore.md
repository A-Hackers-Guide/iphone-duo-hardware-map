# `_UISceneCompanionConfigurableImpl`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `_UISceneCompanionImpl`
- 4 instance variables, 6 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"_UISceneHostingSceneSpecification" _specification;
@"_UICompanionSceneAttributes" _attributes;
@"<NSObject>" _userInfo;
@"UISceneConfiguration" _configuration;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"_UISceneHostingSceneSpecification",R,N,V_specification) specification;
@property (T@"_UICompanionSceneAttributes",R,N,V_attributes) attributes;
```

## Instance methods

```
-[_UISceneCompanionConfigurableImpl debugDescription];
-[_UISceneCompanionConfigurableImpl succinctDescription];
-[_UISceneCompanionConfigurableImpl hash];
-[_UISceneCompanionConfigurableImpl description];
-[_UISceneCompanionConfigurableImpl specification];
-[_UISceneCompanionConfigurableImpl appendDescriptionToStream:];
-[_UISceneCompanionConfigurableImpl attributes];
-[_UISceneCompanionConfigurableImpl isEqual:];
-[_UISceneCompanionConfigurableImpl createInitialConnectionActions];
-[_UISceneCompanionConfigurableImpl initWithSpecification:attributesIdentifier:configuration:userInfo:];
-[_UISceneCompanionConfigurableImpl overrideConfigurationFromV1Registration:];
```
