# `FBSDisplayLayout`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCCoding`, `BSDescriptionProviding`
- 6 instance variables, 11 properties, 28 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _elements;
@"NSDate" _timestamp;
@"FBSDisplayConfiguration" _displayConfiguration;
q _interfaceOrientation;
q _backlightLevel;
q _backlightState;
```

## Properties

```
@property (T@"FBSDisplayConfiguration",&,N,V_displayConfiguration) displayConfiguration;
@property (Tq,N,V_interfaceOrientation) interfaceOrientation;
@property (Tq,N,V_backlightLevel) displayBacklightLevel;
@property (Tq,N,V_backlightState) backlightState;
@property (T@"NSArray",R,C,N,V_elements) elements;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,D,N) bounds;
@property (T@"NSDate",R,N,V_timestamp) timestamp;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBSDisplayLayout removeElement:];
-[FBSDisplayLayout referenceBounds];
-[FBSDisplayLayout setBacklightState:];
-[FBSDisplayLayout interfaceOrientation];
-[FBSDisplayLayout display];
-[FBSDisplayLayout displayConfiguration];
-[FBSDisplayLayout _initWithElements:];
-[FBSDisplayLayout displayType];
-[FBSDisplayLayout addElement:];
-[FBSDisplayLayout elements];
-[FBSDisplayLayout succinctDescriptionBuilder];
-[FBSDisplayLayout setInterfaceOrientation:];
-[FBSDisplayLayout init];
-[FBSDisplayLayout initWithXPCDictionary:];
-[FBSDisplayLayout timestamp];
-[FBSDisplayLayout descriptionWithMultilinePrefix:];
-[FBSDisplayLayout setDisplayBacklightLevel:];
-[FBSDisplayLayout setDisplayConfiguration:];
-[FBSDisplayLayout succinctDescription];
-[FBSDisplayLayout backlightState];
-[FBSDisplayLayout encodeWithXPCDictionary:];
-[FBSDisplayLayout bounds];
-[FBSDisplayLayout description];
-[FBSDisplayLayout finalizeLayout];
-[FBSDisplayLayout isEqual:];
-[FBSDisplayLayout displayBacklightLevel];
-[FBSDisplayLayout _sortElements];
-[FBSDisplayLayout descriptionBuilderWithMultilinePrefix:];
```
