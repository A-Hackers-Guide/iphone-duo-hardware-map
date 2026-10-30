# `PKTitleQuery`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CHQueryDelegate`
- 3 instance variables, 8 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"<PKTitleQueryDelegate>" _delegate;
@"CHTitleQuery" _titleQuery;
@"PKDrawing" _drawing;
```

## Properties

```
@property (T@"CHTitleQuery",&,N,V_titleQuery) titleQuery;
@property (T@"PKDrawing",&,N,V_drawing) drawing;
@property (T@"<PKTitleQueryDelegate>",W,N,V_delegate) delegate;
@property (T@"NSString",R,C,N) transcribedTitle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKTitleQuery drawing];
-[PKTitleQuery pause];
-[PKTitleQuery dealloc];
-[PKTitleQuery start];
-[PKTitleQuery setDrawing:];
-[PKTitleQuery setDelegate:];
-[PKTitleQuery delegate];
-[PKTitleQuery setTitleQuery:];
-[PKTitleQuery titleQuery];
-[PKTitleQuery initWithDrawing:];
-[PKTitleQuery queryDidUpdateResult:];
-[PKTitleQuery transcribedTitle];
```
