# `UIApplicationShortcutIcon`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCCoding`, `NSCopying`
- 1 instance variables, 5 properties, 7 instance methods, 6 class methods

## Instance variables

```
@"SBSApplicationShortcutIcon" _sbsShortcutIcon;
```

## Properties

```
@property (T@"SBSApplicationShortcutIcon",R,N,V_sbsShortcutIcon) sbsShortcutIcon;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIApplicationShortcutIcon iconWithTemplateImageName:];
+[UIApplicationShortcutIcon iconWithSystemImageName:];
+[UIApplicationShortcutIcon iconWithCustomImage:isTemplate:];
+[UIApplicationShortcutIcon _iconWithPrivateSystemImageName:];
+[UIApplicationShortcutIcon iconWithCustomImage:];
+[UIApplicationShortcutIcon iconWithType:];
```

## Instance methods

```
-[UIApplicationShortcutIcon initWithXPCDictionary:];
-[UIApplicationShortcutIcon encodeWithXPCDictionary:];
-[UIApplicationShortcutIcon hash];
-[UIApplicationShortcutIcon copyWithZone:];
-[UIApplicationShortcutIcon isEqual:];
-[UIApplicationShortcutIcon sbsShortcutIcon];
-[UIApplicationShortcutIcon initWithSBSApplicationShortcutIcon:];
```
