# `UISceneSessionActivationRequest`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDebugDescriptionProviding`, `NSCopying`
- 6 instance variables, 10 properties, 17 instance methods, 4 class methods

## Instance variables

```
@"UISceneConfiguration" _configuration;
@"_UISceneConnectionOptionDefinitionPayloadStorage" _definitionPayloadStorage;
@"NSString" _role;
@"UISceneSession" _session;
@"NSUserActivity" _userActivity;
@"UISceneActivationRequestOptions" _options;
```

## Properties

```
@property (T@"_UISceneConnectionOptionDefinitionPayloadStorage",R,N,V_definitionPayloadStorage) _definitionPayloadStorage;
@property (T@"UISceneConfiguration",R,N,V_configuration) _configuration;
@property (T@"NSString",R,N,V_role) role;
@property (T@"UISceneSession",R,N,V_session) session;
@property (T@"NSUserActivity",&,N,V_userActivity) userActivity;
@property (T@"UISceneActivationRequestOptions",C,N,V_options) options;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UISceneSessionActivationRequest request];
+[UISceneSessionActivationRequest _requestWithConfiguration:];
+[UISceneSessionActivationRequest requestWithRole:];
+[UISceneSessionActivationRequest requestWithSession:];
```

## Instance methods

```
-[UISceneSessionActivationRequest setOptions:];
-[UISceneSessionActivationRequest debugDescription];
-[UISceneSessionActivationRequest userActivity];
-[UISceneSessionActivationRequest succinctDescriptionBuilder];
-[UISceneSessionActivationRequest setUserActivity:];
-[UISceneSessionActivationRequest descriptionWithMultilinePrefix:];
-[UISceneSessionActivationRequest _configuration];
-[UISceneSessionActivationRequest succinctDescription];
-[UISceneSessionActivationRequest debugDescriptionWithMultilinePrefix:];
-[UISceneSessionActivationRequest role];
-[UISceneSessionActivationRequest description];
-[UISceneSessionActivationRequest options];
-[UISceneSessionActivationRequest session];
-[UISceneSessionActivationRequest copyWithZone:];
-[UISceneSessionActivationRequest descriptionBuilderWithMultilinePrefix:];
-[UISceneSessionActivationRequest _definitionPayloadStorage];
-[UISceneSessionActivationRequest _initWithSession:role:configuration:];
```
