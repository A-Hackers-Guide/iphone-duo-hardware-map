# `FBSDisplayLayoutPublishing` (protocol)

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 13 instance methods, 0 class methods

## Properties

```
@property (Tq,N) interfaceOrientation;
@property (Tq,N) backlightLevel;
@property (TB,R,N,GisTransitioning) transitioning;
@property (T@"FBSDisplayLayout",R,N) currentLayout;
```

## Instance methods

```
-[FBSDisplayLayoutPublishing interfaceOrientation];
-[FBSDisplayLayoutPublishing setBacklightLevel:];
-[FBSDisplayLayoutPublishing addElement:];
-[FBSDisplayLayoutPublishing backlightLevel];
-[FBSDisplayLayoutPublishing setInterfaceOrientation:];
-[FBSDisplayLayoutPublishing removeObserver:];
-[FBSDisplayLayoutPublishing flush];
-[FBSDisplayLayoutPublishing add:];
-[FBSDisplayLayoutPublishing isTransitioning];
-[FBSDisplayLayoutPublishing remove:];
-[FBSDisplayLayoutPublishing currentLayout];
-[FBSDisplayLayoutPublishing addObserver:];
-[FBSDisplayLayoutPublishing transitionAssertionWithReason:];
```
