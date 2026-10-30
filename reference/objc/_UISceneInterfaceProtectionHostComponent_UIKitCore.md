# `_UISceneInterfaceProtectionHostComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `_UISceneInterfaceProtectionHost`, `_UISceneInterfaceProtectionManagedShieldConfiguration`, `APSubjectMonitor`, `APBaseExtensionShieldViewDelegate`, `BSDescriptionStreaming`, `FBSceneComponent`
- 8 instance variables, 5 properties, 19 instance methods, 0 class methods

## Instance variables

```
{?="isConfiguringSelfMonitoring"b1"isSelfMonitored"b1"hasConfiguredAppProtection"b1} _flags;
@"APSubject" _apSubject;
@"NSString" _appIconBundleIdentifier;
@"NSString" _localizedName;
@"UIView" _shieldParentView;
@"UIView" _shieldViewIfExists;
@ _subjectMonitorRegistry;
@"<BSInvalidatable>" _sheetDisconnectionAssertion;
```

## Properties

```
@property (TB,N) extensionShieldCurrentlyShown;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UISceneInterfaceProtectionHostComponent setLocalizedName:];
-[_UISceneInterfaceProtectionHostComponent debugDescription];
-[_UISceneInterfaceProtectionHostComponent setShieldParentView:];
-[_UISceneInterfaceProtectionHostComponent sceneDidEnterBackground:];
-[_UISceneInterfaceProtectionHostComponent appProtectionSubjectsChanged:forSubscription:];
-[_UISceneInterfaceProtectionHostComponent setScene:];
-[_UISceneInterfaceProtectionHostComponent dealloc];
-[_UISceneInterfaceProtectionHostComponent setExtensionShieldCurrentlyShown:];
-[_UISceneInterfaceProtectionHostComponent sceneDidInvalidate:];
-[_UISceneInterfaceProtectionHostComponent succinctDescription];
-[_UISceneInterfaceProtectionHostComponent setAppIconBundleIdentifier:];
-[_UISceneInterfaceProtectionHostComponent extensionShieldCurrentlyShown];
-[_UISceneInterfaceProtectionHostComponent setUnderAppProtection:];
-[_UISceneInterfaceProtectionHostComponent description];
-[_UISceneInterfaceProtectionHostComponent appendDescriptionToStream:];
-[_UISceneInterfaceProtectionHostComponent configureSelfMonitoringWithConfiguration:];
-[_UISceneInterfaceProtectionHostComponent sceneWillEnterForeground:];
-[_UISceneInterfaceProtectionHostComponent setAPSubject:];
-[_UISceneInterfaceProtectionHostComponent shieldViewUnlockButtonPressed:];
```
