# `SBSystemApertureAlertItemPresenter`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBAlertItemPresenter`
- 2 instance variables, 6 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"<SAElementRegistering>" _registrar;
@"NSMapTable" _elementsToAssertions;
```

## Properties

```
@property (T@"<SAElementRegistering>",R,W,N,V_registrar) registrar;
@property (T@"NSMapTable",R,N,V_elementsToAssertions) elementsToAssertions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSystemApertureAlertItemPresenter elementsToAssertions];
-[SBSystemApertureAlertItemPresenter canPresentMultipleAlertItemsSimultaneously];
-[SBSystemApertureAlertItemPresenter dismissAlertItem:animated:completion:];
-[SBSystemApertureAlertItemPresenter initWithElementRegistrar:];
-[SBSystemApertureAlertItemPresenter presentAlertItem:animated:completion:];
-[SBSystemApertureAlertItemPresenter presentsAlertItemsModally];
-[SBSystemApertureAlertItemPresenter registrar];
```
