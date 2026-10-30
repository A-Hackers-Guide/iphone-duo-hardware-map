# `ICDocCamProcessingBlocker`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"<ICDocCamProcessingBlockerDelegate>" _delegate;
@"NSMutableSet" _blockerSet;
```

## Properties

```
@property (T@"<ICDocCamProcessingBlockerDelegate>",W,N,V_delegate) delegate;
@property (T@"NSMutableSet",&,N,V_blockerSet) blockerSet;
```

## Instance methods

```
-[ICDocCamProcessingBlocker initWithDelegate:];
-[ICDocCamProcessingBlocker setDelegate:];
-[ICDocCamProcessingBlocker delegate];
-[ICDocCamProcessingBlocker blocked];
-[ICDocCamProcessingBlocker addBlockerOfType:clearRectangles:clearQueue:];
-[ICDocCamProcessingBlocker blockerSet];
-[ICDocCamProcessingBlocker removeBlockerOfType:];
-[ICDocCamProcessingBlocker setBlockerSet:];
```
