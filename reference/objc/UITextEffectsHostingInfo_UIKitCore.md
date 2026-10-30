# `UITextEffectsHostingInfo`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UISceneBasedObject`
- 3 instance variables, 9 properties, 10 instance methods, 1 class methods

## Instance variables

```
Q _hostedUseCount;
@"UIWindowScene" _scene;
@"NSDictionary" _perSceneOptions;
```

## Properties

```
@property (T@"NSDictionary",&,N,V_perSceneOptions) perSceneOptions;
@property (T@"UIWindowScene",&,N,V_scene) scene;
@property (TB,N) useHostedInstance;
@property (T@"UIWindowScene",R) _intendedScene;
@property (T@"NSDictionary",R) _options;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UITextEffectsHostingInfo hostingInfoForWindowScene:];
```

## Instance methods

```
-[UITextEffectsHostingInfo _options];
-[UITextEffectsHostingInfo setPerSceneOptions:];
-[UITextEffectsHostingInfo perSceneOptions];
-[UITextEffectsHostingInfo setScene:];
-[UITextEffectsHostingInfo scene];
-[UITextEffectsHostingInfo _matchingOptions:];
-[UITextEffectsHostingInfo _intendedScene];
-[UITextEffectsHostingInfo setUseHostedInstance:];
-[UITextEffectsHostingInfo _initWithScene:options:];
-[UITextEffectsHostingInfo useHostedInstance];
```
