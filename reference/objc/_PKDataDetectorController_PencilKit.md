# `_PKDataDetectorController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKDataDetectorItemDelegate`
- 3 instance variables, 6 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _currentDataDetectorItems;
{?="delegateSupportsItemsDidChange"b1} _delegateFlags;
@"<_PKDataDetectorControllerDelegate>" _delegate;
```

## Properties

```
@property (T@"<_PKDataDetectorControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"NSArray",R,N) currentItems;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_PKDataDetectorController init];
-[_PKDataDetectorController setDelegate:];
-[_PKDataDetectorController hitTest:];
-[_PKDataDetectorController delegate];
-[_PKDataDetectorController currentItems];
-[_PKDataDetectorController dataDetectorItemAllItems:];
```
