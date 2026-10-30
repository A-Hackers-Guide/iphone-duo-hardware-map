# `UIIndexBarEntry`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 7 properties, 13 instance methods, 7 class methods

## Instance variables

```
@"NSString" _title;
@"NSString" _shortTitle;
q _type;
@"UIImage" _image;
@"NSIndexPath" _indexPath;
```

## Properties

```
@property (Tq,N,V_type) type;
@property (T@"NSString",C,N,V_title) title;
@property (T@"NSString",R,N) effectiveShortTitle;
@property (T@"UIImage",&,N,V_image) image;
@property (T@"NSIndexPath",C,N,V_indexPath) indexPath;
@property (TB,R,N) hasPoundTitle;
@property (T@"NSString",C,N,V_shortTitle) shortTitle;
```

## Class methods

```
+[UIIndexBarEntry entryForNumbers];
+[UIIndexBarEntry entryWithTitle:];
+[UIIndexBarEntry _dotImageInView:];
+[UIIndexBarEntry _externalDotImageInView:];
+[UIIndexBarEntry entryForDotInView:];
+[UIIndexBarEntry entryForSearch];
+[UIIndexBarEntry entryWithType:];
```

## Instance methods

```
-[UIIndexBarEntry indexPath];
-[UIIndexBarEntry shortTitle];
-[UIIndexBarEntry setType:];
-[UIIndexBarEntry type];
-[UIIndexBarEntry title];
-[UIIndexBarEntry setIndexPath:];
-[UIIndexBarEntry description];
-[UIIndexBarEntry setTitle:];
-[UIIndexBarEntry image];
-[UIIndexBarEntry setImage:];
-[UIIndexBarEntry effectiveShortTitle];
-[UIIndexBarEntry hasPoundTitle];
-[UIIndexBarEntry setShortTitle:];
```
