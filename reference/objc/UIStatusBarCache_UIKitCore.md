# `UIStatusBarCache`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"CPBitmapStore" _store;
B _writeable;
```

## Properties

```
@property (TB,R,N,GisWriteable,V_writeable) writeable;
```

## Class methods

```
+[UIStatusBarCache sharedInstance];
```

## Instance methods

```
-[UIStatusBarCache init];
-[UIStatusBarCache cacheImage:named:forGroup:];
-[UIStatusBarCache imageNamed:forGroup:withScale:];
-[UIStatusBarCache isWriteable];
-[UIStatusBarCache removeImagesInGroup:];
```
