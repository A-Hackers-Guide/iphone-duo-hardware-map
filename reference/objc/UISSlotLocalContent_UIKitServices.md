# `UISSlotLocalContent`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UISSlotAnyContent`
- 3 instance variables, 8 properties, 9 instance methods, 3 class methods

## Instance variables

```
C _contentScale;
{CGSize="width"d"height"d} _contentSize;
^{CGImage=} _localImage;
```

## Properties

```
@property (TC,R,N) contentScale;
@property (T{CGSize=dd},R,N) contentSize;
@property (TB,R,N) isRemote;
@property (TB,R,N) shouldReplaceExistingContent;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UISSlotLocalContent contentWithDrawing:style:];
+[UISSlotLocalContent contentWithDrawing:scale:range:];
+[UISSlotLocalContent contentWithImage:scale:];
```

## Instance methods

```
-[UISSlotLocalContent isRemote];
-[UISSlotLocalContent dealloc];
-[UISSlotLocalContent contentSize];
-[UISSlotLocalContent contentScale];
-[UISSlotLocalContent image];
-[UISSlotLocalContent deleteFromLayerContext:];
-[UISSlotLocalContent shouldReplaceExistingContent];
-[UISSlotLocalContent initWithDrawing:scale:range:];
-[UISSlotLocalContent initWithImage:scale:];
```
