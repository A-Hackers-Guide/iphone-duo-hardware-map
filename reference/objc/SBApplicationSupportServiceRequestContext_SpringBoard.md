# `SBApplicationSupportServiceRequestContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 0 properties, 17 instance methods, 4 class methods

## Instance variables

```
B _hostIsSpringBoard;
@"SBApplication" _app;
@"SBApplication" _hostApp;
@"SBApplication" _extensionContainingApp;
@"UISApplicationInitializationContext" _selfLock_applicationInitializationContext;
@"FBSDisplayConfiguration" _launchDisplayConfiguration;
@"<SBApplicationSupportServiceRequestPersistenceIdentifierProvider>" _preferredAppPersistenceIDProvider;
@"<SBApplicationSceneIdentityCreating>" _preferredAppSceneIdentityCreator;
@"<SBApplicationSupportServiceRequestSceneIdentityTokenProvider>" _preferredSceneIdentityTokenProvider;
```

## Class methods

```
+[SBApplicationSupportServiceRequestContext _hostProcessForProcess:];
+[SBApplicationSupportServiceRequestContext hostingApplicationBundleIDForPid:];
+[SBApplicationSupportServiceRequestContext initializationContextForClient:completion:];
+[SBApplicationSupportServiceRequestContext shouldOverrideClientInitialization:];
```

## Instance methods

```
-[SBApplicationSupportServiceRequestContext _main_launchDisplayContext];
-[SBApplicationSupportServiceRequestContext initWithClient:host:];
-[SBApplicationSupportServiceRequestContext initWithApplication:launchDisplayConfiguration:persistenceIdentifierProvider:sceneIdentityCreator:sceneIdentityTokenProvider:];
-[SBApplicationSupportServiceRequestContext initWithApplication:launchDisplayConfiguration:];
-[SBApplicationSupportServiceRequestContext _main_appSceneIdentityCreator];
-[SBApplicationSupportServiceRequestContext _main_deviceContext];
-[SBApplicationSupportServiceRequestContext _main_applicationInitializationContext];
-[SBApplicationSupportServiceRequestContext _main_embeddedDisplayContext];
-[SBApplicationSupportServiceRequestContext _main_effectiveScreenType];
-[SBApplicationSupportServiceRequestContext _main_appPersistenceIDProvider];
-[SBApplicationSupportServiceRequestContext _main_effectiveClassicMode];
-[SBApplicationSupportServiceRequestContext applicationInitializationContextWithCompletion:];
-[SBApplicationSupportServiceRequestContext _main_effectiveApplicationForCompatibility];
-[SBApplicationSupportServiceRequestContext _main_applyClassicModeLiesIfNecessaryToDisplayContext:];
-[SBApplicationSupportServiceRequestContext _main_sceneIdentityTokenProvider];
-[SBApplicationSupportServiceRequestContext _main_persistenceIDs];
-[SBApplicationSupportServiceRequestContext _main_displayContextForDisplayConfiguration:];
```
