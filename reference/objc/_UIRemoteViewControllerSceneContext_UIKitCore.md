# `_UIRemoteViewControllerSceneContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`, `_UISystemShellSceneHostingEnvironmentClient`, `_UISceneRenderingEnvironmentClientInternal`
- 10 instance variables, 13 properties, 17 instance methods, 1 class methods

## Instance variables

```
B _isCapturingContentForAdditionalRenderingDestination;
B _prefersContentProtection;
B _enhancedWindowingEnabled;
@"NSString" _systemShellHostingSpaceIdentifier;
@"NSString" _systemDisplayIdentifier;
@"FBSDisplayIdentity" _displayIdentity;
q _screenReferenceDisplayModeStatus;
d _systemReferenceAngle;
Q _systemReferenceAngleMode;
@"NSString" _hardwareKeyboardExclusivityIdentifier;
```

## Properties

```
@property (T@"NSString",R,N,V_systemShellHostingSpaceIdentifier) systemShellHostingSpaceIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIScene<_UISceneUIWindowHosting>",R,W,N) _windowHostingScene;
@property (Td,R,N) screenBrightness;
@property (TB,R,N,V_isCapturingContentForAdditionalRenderingDestination) isCapturingContentForAdditionalRenderingDestination;
@property (T@"NSString",R,C,N,V_systemDisplayIdentifier) systemDisplayIdentifier;
@property (Td,N) preferredScreenBrightness;
@property (TB,N,V_prefersContentProtection) prefersContentProtection;
@property (T@"_UIUserInterfaceSizeClassResolver",R,N) horizontalSizeClassResolver;
@property (T@"_UIUserInterfaceSizeClassResolver",R,N) verticalSizeClassResolver;
```

## Class methods

```
+[_UIRemoteViewControllerSceneContext supportsSecureCoding];
```

## Instance methods

```
-[_UIRemoteViewControllerSceneContext screenBrightness];
-[_UIRemoteViewControllerSceneContext _windowHostingScene];
-[_UIRemoteViewControllerSceneContext systemShellHostingSpaceIdentifier];
-[_UIRemoteViewControllerSceneContext horizontalSizeClassResolver];
-[_UIRemoteViewControllerSceneContext systemDisplayIdentifier];
-[_UIRemoteViewControllerSceneContext preferredScreenBrightness];
-[_UIRemoteViewControllerSceneContext prefersContentProtection];
-[_UIRemoteViewControllerSceneContext encodeWithCoder:];
-[_UIRemoteViewControllerSceneContext description];
-[_UIRemoteViewControllerSceneContext initWithCoder:];
-[_UIRemoteViewControllerSceneContext verticalSizeClassResolver];
-[_UIRemoteViewControllerSceneContext copyWithZone:];
-[_UIRemoteViewControllerSceneContext isEqual:];
-[_UIRemoteViewControllerSceneContext setPreferredScreenBrightness:];
-[_UIRemoteViewControllerSceneContext isCapturingContentForAdditionalRenderingDestination];
-[_UIRemoteViewControllerSceneContext setPrefersContentProtection:];
-[_UIRemoteViewControllerSceneContext initWithDisplayIdentity:screenReferenceDisplayModeStatus:enhancedWindowEnabled:systemReferenceAngle:systemReferenceAngleMode:isCapturingContentForAdditionalRenderingDestination:hardwareKeyboardExclusivityIdentifier:systemShellHostingSpaceIdentifier:systemDisplayIdentifier:];
```
