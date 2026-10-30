# `UIDebuggingSpecViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UIImagePickerControllerDelegate`, `UINavigationControllerDelegate`, `UICollectionViewDataSource`, `UICollectionViewDelegate`, `UIDebuggingInformationViewController`
- 6 instance variables, 10 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"UIView" _spec;
@"NSMutableArray" _specImages;
d _originalOpacity;
@"UICollectionView" _collectionView;
@"UICollectionViewFlowLayout" _flowLayout;
{CGPoint="x"d"y"d} _origin;
```

## Properties

```
@property (T@"UIView",&,N,V_spec) spec;
@property (T@"NSMutableArray",&,N,V_specImages) specImages;
@property (T{CGPoint=dd},N,V_origin) origin;
@property (Td,N,V_originalOpacity) originalOpacity;
@property (T@"UICollectionView",&,N,V_collectionView) collectionView;
@property (T@"UICollectionViewFlowLayout",&,N,V_flowLayout) flowLayout;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIDebuggingSpecViewController setSpec:];
-[UIDebuggingSpecViewController origin];
-[UIDebuggingSpecViewController collectionView:numberOfItemsInSection:];
-[UIDebuggingSpecViewController collectionView:didSelectItemAtIndexPath:];
-[UIDebuggingSpecViewController collectionView:cellForItemAtIndexPath:];
-[UIDebuggingSpecViewController spec];
-[UIDebuggingSpecViewController numberOfSectionsInCollectionView:];
-[UIDebuggingSpecViewController collectionView];
-[UIDebuggingSpecViewController viewDidLoad];
-[UIDebuggingSpecViewController initWithNibName:bundle:];
-[UIDebuggingSpecViewController setCollectionView:];
-[UIDebuggingSpecViewController setOrigin:];
-[UIDebuggingSpecViewController imagePickerControllerDidCancel:];
-[UIDebuggingSpecViewController originalOpacity];
-[UIDebuggingSpecViewController flowLayout];
-[UIDebuggingSpecViewController gotDeleteGesture:];
-[UIDebuggingSpecViewController gotPanGesture:];
-[UIDebuggingSpecViewController hideImage];
-[UIDebuggingSpecViewController imagePickerController:didFinishPickingMediaWithInfo:];
-[UIDebuggingSpecViewController prepareForMediaBrowser];
-[UIDebuggingSpecViewController setFlowLayout:];
-[UIDebuggingSpecViewController setOriginalOpacity:];
-[UIDebuggingSpecViewController setSpecImages:];
-[UIDebuggingSpecViewController specImages];
-[UIDebuggingSpecViewController startMediaBrowserFromViewController:];
```
