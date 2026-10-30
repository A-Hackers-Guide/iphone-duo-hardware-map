# `UISceneAccessoryRegistration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UISceneCompanionRegistration`, `BSDescriptionStreaming`
- 4 instance variables, 8 properties, 16 instance methods, 0 class methods

## Instance variables

```
_uuid;
@"<_UISceneCompanionImpl>" _companion;
_flags;
_providingViewControllerStorage;
```

## Properties

```
@property (TB,N) enabled;
@property (TB,N,R) available;
@property (TB,N) _isProvidingViewControllerVisible;
@property (T@"UIViewController",N,W) _providingViewController;
@property (T@"NSUUID",N,R) _identifier;
@property (T@"<_UISceneCompanionImpl>",N,R,V_companion) _companion;
@property (T@"NSString",N,R) description;
@property (T@"NSString",N,R) debugDescription;
```

## Instance methods

```
-[UISceneAccessoryRegistration isAvailable];
-[UISceneAccessoryRegistration debugDescription];
-[UISceneAccessoryRegistration init];
-[UISceneAccessoryRegistration isEnabled];
-[UISceneAccessoryRegistration succinctDescription];
-[UISceneAccessoryRegistration setEnabled:];
-[UISceneAccessoryRegistration description];
-[UISceneAccessoryRegistration appendDescriptionToStream:];
-[UISceneAccessoryRegistration _identifier];
-[UISceneAccessoryRegistration _companion];
-[UISceneAccessoryRegistration _isProvidingViewControllerVisible];
-[UISceneAccessoryRegistration _providingViewController];
-[UISceneAccessoryRegistration _setAvailable:];
-[UISceneAccessoryRegistration _setProvidingViewController:];
-[UISceneAccessoryRegistration _setProvidingViewControllerVisible:];
-[UISceneAccessoryRegistration initWithCompanion:];
```
