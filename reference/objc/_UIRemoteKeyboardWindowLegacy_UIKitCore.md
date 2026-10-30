# `_UIRemoteKeyboardWindowLegacy`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIRemoteKeyboardWindow`
- Protocols: `_UIContextCustomBinding`, `_UIScreenBasedObject`, `_UIRemoteKeyboardWindowDelegate`
- 2 instance variables, 9 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"UIScreen" _intendedScreen;
@"NSDictionary" _options;
```

## Properties

```
@property (T@"CAContext",W,N,S_setBoundContext:) _boundContext;
@property (T@"_UIContextBinder",W,N,S_setContextBinder:) _contextBinder;
@property (T{?=@BBBBBBBBBB},R,N) _bindingDescription;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIScreen",R,V_intendedScreen) _intendedScreen;
@property (T@"NSDictionary",R,V_options) _options;
```

## Instance methods

```
-[_UIRemoteKeyboardWindowLegacy _options];
-[_UIRemoteKeyboardWindowLegacy _remoteKeyboardWindowWillInvalidate:];
-[_UIRemoteKeyboardWindowLegacy _initWithScreen:options:];
-[_UIRemoteKeyboardWindowLegacy _matchingOptions:];
-[_UIRemoteKeyboardWindowLegacy _intendedScreen];
-[_UIRemoteKeyboardWindowLegacy _isWindowServerHostingManaged];
-[_UIRemoteKeyboardWindowLegacy _wantsSceneAssociation];
-[_UIRemoteKeyboardWindowLegacy attachBindable];
-[_UIRemoteKeyboardWindowLegacy detachBindable];
-[_UIRemoteKeyboardWindowLegacy shouldAttachBindable];
-[_UIRemoteKeyboardWindowLegacy shouldDetachBindable];
```
