# `FBSApplicationTerminationAssertion`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 3 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"BKSTerminationAssertion" _assertion;
q _assertionState;
@"NSString" _bundleID;
@"NSString" _reason;
```

## Properties

```
@property (T@"NSString",R,C,N,V_bundleID) bundleID;
@property (T@"NSString",R,C,N,V_reason) reason;
@property (Tq,R,N) assertionState;
```

## Instance methods

```
-[FBSApplicationTerminationAssertion dealloc];
-[FBSApplicationTerminationAssertion invalidate];
-[FBSApplicationTerminationAssertion description];
-[FBSApplicationTerminationAssertion bundleID];
-[FBSApplicationTerminationAssertion reason];
-[FBSApplicationTerminationAssertion assertionState];
-[FBSApplicationTerminationAssertion initWithBundleID:reason:acquisitionHandler:];
```
