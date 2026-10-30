# `_UIDocumentURLChangeObserver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSFilePresenter`
- 3 instance variables, 10 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSURL" _presentedItemURL;
@"NSOperationQueue" _presentedItemOperationQueue;
@? _changeHandler;
```

## Properties

```
@property (T@?,C,N,V_changeHandler) changeHandler;
@property (TB,R,N,GisObserving) observing;
@property (T@"NSURL",R,C,V_presentedItemURL) presentedItemURL;
@property (T@"NSOperationQueue",R,&,V_presentedItemOperationQueue) presentedItemOperationQueue;
@property (T@"NSURL",?,R,C) primaryPresentedItemURL;
@property (T@"NSSet",?,R) observedPresentedItemUbiquityAttributes;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIDocumentURLChangeObserver stopObserving];
-[_UIDocumentURLChangeObserver initWithFileURL:];
-[_UIDocumentURLChangeObserver presentedItemOperationQueue];
-[_UIDocumentURLChangeObserver isObserving];
-[_UIDocumentURLChangeObserver presentedItemURL];
-[_UIDocumentURLChangeObserver setChangeHandler:];
-[_UIDocumentURLChangeObserver presentedItemDidMoveToURL:];
-[_UIDocumentURLChangeObserver changeHandler];
-[_UIDocumentURLChangeObserver presentedItemDidChange];
-[_UIDocumentURLChangeObserver startObservingWithChangeHandler:];
```
