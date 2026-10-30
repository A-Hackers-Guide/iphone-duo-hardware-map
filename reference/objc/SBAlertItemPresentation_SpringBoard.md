# `SBAlertItemPresentation`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 2 instance variables, 6 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"SBAlertItem" _alertItem;
@"<SBAlertItemPresenter>" _presenter;
```

## Properties

```
@property (T@"SBAlertItem",&,N,V_alertItem) alertItem;
@property (T@"<SBAlertItemPresenter>",&,N,V_presenter) presenter;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAlertItemPresentation setAlertItem:];
-[SBAlertItemPresentation presenter];
-[SBAlertItemPresentation alertItem];
-[SBAlertItemPresentation succinctDescriptionBuilder];
-[SBAlertItemPresentation setPresenter:];
-[SBAlertItemPresentation initWithAlertItem:presenter:];
-[SBAlertItemPresentation descriptionWithMultilinePrefix:];
-[SBAlertItemPresentation succinctDescription];
-[SBAlertItemPresentation hash];
-[SBAlertItemPresentation description];
-[SBAlertItemPresentation isEqual:];
-[SBAlertItemPresentation descriptionBuilderWithMultilinePrefix:];
```
