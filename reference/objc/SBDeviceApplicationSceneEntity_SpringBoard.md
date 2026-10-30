# `SBDeviceApplicationSceneEntity`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBApplicationSceneEntity`
- 0 instance variables, 1 properties, 19 instance methods, 8 class methods

## Properties

```
@property (T@"SBDeviceApplicationSceneHandle",R,D,N) sceneHandle;
```

## Class methods

```
+[SBDeviceApplicationSceneEntity newEntityWithApplication:sceneIdentityProvider:displayIdentity:];
+[SBDeviceApplicationSceneEntity defaultEntityWithApplication:sceneIdentityProvider:displayIdentity:];
+[SBDeviceApplicationSceneEntity defaultEntityWithApplication:targetContentIdentifier:sceneIdentityProvider:displayIdentity:];
+[SBDeviceApplicationSceneEntity defaultEntityWithApplicationForMainDisplay:];
+[SBDeviceApplicationSceneEntity defaultEntityWithApplicationForMainDisplay:targetContentIdentifier:];
+[SBDeviceApplicationSceneEntity entityWithApplication:scenePersistenceIdentifier:sceneIdentityProvider:displayIdentity:];
+[SBDeviceApplicationSceneEntity entityWithApplicationForMainDisplay:withScenePersistenceIdentifier:];
+[SBDeviceApplicationSceneEntity newEntityWithApplicationForMainDisplay:];
```

## Instance methods

```
-[SBDeviceApplicationSceneEntity wantsExclusiveForeground];
-[SBDeviceApplicationSceneEntity initWithApplication:generatingNewPrimarySceneIfRequired:sceneIdentityProvider:displayIdentity:];
-[SBDeviceApplicationSceneEntity initWithApplication:uniqueIdentifier:targetContentIdentifier:sceneIdentityProvider:displayIdentity:];
-[SBDeviceApplicationSceneEntity initWithApplication:generatingNewSceneIfRequiredWithSpecification:sceneIdentityProvider:displayIdentity:];
-[SBDeviceApplicationSceneEntity isDeviceApplicationSceneEntity];
-[SBDeviceApplicationSceneEntity initWithApplication:sceneIdentityProvider:displayIdentity:];
-[SBDeviceApplicationSceneEntity initWithApplicationForMainDisplay:generatingNewPrimarySceneIfRequired:];
-[SBDeviceApplicationSceneEntity initWithApplicationForMainDisplay:targetContentIdentifier:];
-[SBDeviceApplicationSceneEntity supportsPresentationAtAnySize];
-[SBDeviceApplicationSceneEntity initWithApplicationSceneHandle:];
-[SBDeviceApplicationSceneEntity initWithApplicationForMainDisplay:generatingNewSceneIfRequiredWithSpecification:];
-[SBDeviceApplicationSceneEntity initWithApplication:targetContentIdentifier:sceneIdentityProvider:displayIdentity:];
-[SBDeviceApplicationSceneEntity supportedLayoutRoles];
-[SBDeviceApplicationSceneEntity supportsSplitView];
-[SBDeviceApplicationSceneEntity initWithApplicationForMainDisplay:uniqueIdentifier:];
-[SBDeviceApplicationSceneEntity initWithApplication:uniqueIdentifier:sceneIdentityProvider:displayIdentity:];
-[SBDeviceApplicationSceneEntity deviceApplicationSceneEntity];
-[SBDeviceApplicationSceneEntity initWithApplication:uniqueIdentifier:targetContentIdentifier:sceneIdentityProvider:displayIdentity:isSecure:];
-[SBDeviceApplicationSceneEntity initWithApplicationForMainDisplay:];
```
