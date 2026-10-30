# `UISceneSession`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDebugDescriptionProviding`, `NSSecureCoding`
- 8 instance variables, 16 properties, 38 instance methods, 1 class methods

## Instance variables

```
@"UIScene" _scene;
@"NSString" _role;
@"NSString" _persistentIdentifier;
@"UISceneConfiguration" _configuration;
@"NSUserActivity" _stateRestorationActivity;
@"NSDictionary" _userInfo;
@"NSDictionary" _internalUserInfo;
{?="_stateRestorationActivityIsDirty"b1"_stateRestorationActivityIsCurrent"b1"_trackingSessionRequest"b1"_configurationIsDirty"b1"_userInfoIsDirty"b1"_userInfoIsCurrent"b1"_internalUserInfoIsDirty"b1"_internalUserInfoIsCurrent"b1"_isInternal"b1} _sessionFlags;
```

## Properties

```
@property (TB,R,N,G_isInternal) _internal;
@property (TB,R,N) _configurationNeedsReevalulation;
@property (TB,N,S_setTrackingRefreshRequest:) _trackingRefreshRequest;
@property (TB,N,S_setConfigurationIsDirty:) _configurationIsDirty;
@property (TB,N,S_setUserInfoIsDirty:) _userInfoIsDirty;
@property (TB,N,S_setStateRestorationActivityIsDirty:) _stateRestorationActivityIsDirty;
@property (T@"UIScene",R,W,N,V_scene) scene;
@property (T@"NSString",R,N,V_role) role;
@property (T@"UISceneConfiguration",R,C,N) configuration;
@property (T@"NSString",R,N,V_persistentIdentifier) persistentIdentifier;
@property (T@"NSUserActivity",&,N) stateRestorationActivity;
@property (T@"NSDictionary",C,N) userInfo;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UISceneSession supportsSecureCoding];
```

## Instance methods

```
-[UISceneSession persistentIdentifier];
-[UISceneSession debugDescription];
-[UISceneSession succinctDescriptionBuilder];
-[UISceneSession _userInfoIsDirty];
-[UISceneSession stateRestorationActivity];
-[UISceneSession _initWithPersistentIdentifier:sessionRole:configurationName:];
-[UISceneSession _configurationIsDirty];
-[UISceneSession _copyWithoutUserInfo];
-[UISceneSession userInfo];
-[UISceneSession _isInternal];
-[UISceneSession setStateRestorationActivity:];
-[UISceneSession setUserInfo:];
-[UISceneSession _loadStateRestorationActivityIfNeeded];
-[UISceneSession descriptionWithMultilinePrefix:];
-[UISceneSession _init];
-[UISceneSession succinctDescription];
-[UISceneSession _configurationNeedsReevalulation];
-[UISceneSession configuration];
-[UISceneSession debugDescriptionWithMultilinePrefix:];
-[UISceneSession scene];
-[UISceneSession _setTrackingRefreshRequest:];
-[UISceneSession _updateConfiguration:];
-[UISceneSession encodeWithCoder:];
-[UISceneSession _stateRestorationActivityIsDirty];
-[UISceneSession role];
-[UISceneSession hash];
-[UISceneSession description];
-[UISceneSession _resetStateRestorationToActivity:];
-[UISceneSession _trackingRefreshRequest];
-[UISceneSession initWithCoder:];
-[UISceneSession _setUserInfoIsDirty:];
-[UISceneSession _setScene:];
-[UISceneSession _clearAllDirtyFlags];
-[UISceneSession isEqual:];
-[UISceneSession _setStateRestorationActivityIsDirty:];
-[UISceneSession descriptionBuilderWithMultilinePrefix:];
-[UISceneSession _setConfigurationIsDirty:];
-[UISceneSession _loadUserInfo];
```
