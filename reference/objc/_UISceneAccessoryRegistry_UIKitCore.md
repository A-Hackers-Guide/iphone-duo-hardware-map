# `_UISceneAccessoryRegistry`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`, `BSDescriptionStreaming`
- 3 instance variables, 5 properties, 14 instance methods, 0 class methods

## Instance variables

```
? delegate;
_collector;
_registrationsByID;
```

## Properties

```
@property (T@"<_UISceneAccessoryRegistryDelegate>",N,W,Vdelegate) delegate;
@property (T@"<_UISceneAccessoryRegistrationCollecting>",N,R) collector;
@property (T@"NSArray",N,R) registrations;
@property (T@"NSString",N,R) description;
@property (T@"NSString",N,R) debugDescription;
```

## Instance methods

```
-[_UISceneAccessoryRegistry debugDescription];
-[_UISceneAccessoryRegistry registrations];
-[_UISceneAccessoryRegistry init];
-[_UISceneAccessoryRegistry dealloc];
-[_UISceneAccessoryRegistry succinctDescription];
-[_UISceneAccessoryRegistry invalidate];
-[_UISceneAccessoryRegistry setDelegate:];
-[_UISceneAccessoryRegistry delegate];
-[_UISceneAccessoryRegistry description];
-[_UISceneAccessoryRegistry appendDescriptionToStream:];
-[_UISceneAccessoryRegistry appendRegistration:];
-[_UISceneAccessoryRegistry collector];
-[_UISceneAccessoryRegistry examineRegistrations:];
-[_UISceneAccessoryRegistry removeRegistrationWithId:];
```
