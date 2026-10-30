# `CSTraitAwareAppHostContextProviding` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 2 properties, 6 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,N) hostedAppBundleIdentifier;
@property (TB,R,N) hostedAppShouldHideHomeGrabberView;
```

## Instance methods

```
-[CSTraitAwareAppHostContextProviding hostedAppBundleIdentifier];
-[CSTraitAwareAppHostContextProviding hostedAppShouldHideHomeGrabberView];
-[CSTraitAwareAppHostContextProviding hostedAppShouldInvalidateUponDeactivation];
-[CSTraitAwareAppHostContextProviding appendToHostedAppSceneSettings:];
-[CSTraitAwareAppHostContextProviding hostedAppShouldReactivateUponDestruction];
-[CSTraitAwareAppHostContextProviding hostedAppShouldDeactivateAfterDisappearance];
```
