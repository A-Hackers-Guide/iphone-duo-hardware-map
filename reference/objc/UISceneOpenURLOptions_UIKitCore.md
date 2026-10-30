# `UISceneOpenURLOptions`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 12 instance methods, 2 class methods

## Instance variables

```
@"NSString" _sourceApp;
@"BSProcessHandle" _sourceProcessHandle;
@"<NSObject>" _annotation;
B _openInPlace;
@"UIEventAttribution" _eventAttribution;
B _openAsDownload;
q _contentOwner;
```

## Properties

```
@property (T@"BSProcessHandle",R,N,V_sourceProcessHandle) _sourceProcessHandle;
@property (TB,R,N,V_openAsDownload) _openAsDownload;
@property (Tq,R,N,V_contentOwner) _contentOwner;
@property (T@"NSString",R,N,V_sourceApp) sourceApplication;
@property (T@,R,N,V_annotation) annotation;
@property (TB,R,N,V_openInPlace) openInPlace;
@property (T@"UIEventAttribution",R,N,V_eventAttribution) eventAttribution;
```

## Class methods

```
+[UISceneOpenURLOptions _optionsFromPayload:sourceProcessHandle:];
+[UISceneOpenURLOptions _optionsFromDictionary:];
```

## Instance methods

```
-[UISceneOpenURLOptions sourceApplication];
-[UISceneOpenURLOptions _openAsDownload];
-[UISceneOpenURLOptions _contentOwner];
-[UISceneOpenURLOptions _initWithSourceApplication:processHandle:annotation:openInPlace:];
-[UISceneOpenURLOptions _sourceProcessHandle];
-[UISceneOpenURLOptions annotation];
-[UISceneOpenURLOptions hash];
-[UISceneOpenURLOptions description];
-[UISceneOpenURLOptions openInPlace];
-[UISceneOpenURLOptions isEqual:];
-[UISceneOpenURLOptions eventAttribution];
-[UISceneOpenURLOptions _initWithSourceApplication:processHandle:annotation:openInPlace:eventAttribution:openAsDownload:contentOwner:];
```
