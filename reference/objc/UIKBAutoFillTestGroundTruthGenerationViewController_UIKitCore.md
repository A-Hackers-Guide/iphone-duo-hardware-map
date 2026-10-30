# `UIKBAutoFillTestGroundTruthGenerationViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UIKBAutoFillTestTaggerViewDelegate`
- 9 instance variables, 6 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"UIKBAutoFillTestViewController" _testViewController;
@"UIKBAutoFillTestExpectedResult" _expectedResult;
@"UIScrollView" _scrollView;
@"UIKBAutoFillTestTaggerView" _taggerView;
@"NSLayoutConstraint" _scrollViewBottomConstraint;
@"UIView" _highlightView;
@"UIView" _highlightBox;
@"UIBarButtonItem" _doneBarButtonItem;
@"<UIKBAutoFillTestGroundTruthGenerationViewControllerDelegate>" _delegate;
```

## Properties

```
@property (T@"<UIKBAutoFillTestGroundTruthGenerationViewControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"UIKBAutoFillTestViewController",R,N,V_testViewController) testViewController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIKBAutoFillTestGroundTruthGenerationViewController viewDidLoad];
-[UIKBAutoFillTestGroundTruthGenerationViewController setDelegate:];
-[UIKBAutoFillTestGroundTruthGenerationViewController viewDidAppear:];
-[UIKBAutoFillTestGroundTruthGenerationViewController delegate];
-[UIKBAutoFillTestGroundTruthGenerationViewController _cancelBarButtonItemAction:];
-[UIKBAutoFillTestGroundTruthGenerationViewController _enumerateSubviewsOfRootView:usingBlock:];
-[UIKBAutoFillTestGroundTruthGenerationViewController _moveTaggerHighlightViewOverView:];
-[UIKBAutoFillTestGroundTruthGenerationViewController _removeTaggerHighlightView];
-[UIKBAutoFillTestGroundTruthGenerationViewController initWithAutoFillTestViewController:];
-[UIKBAutoFillTestGroundTruthGenerationViewController taggerView:didTagFormRequest:withSelectedType:];
-[UIKBAutoFillTestGroundTruthGenerationViewController taggerView:didTagTextFieldRequest:withSelectedType:];
-[UIKBAutoFillTestGroundTruthGenerationViewController taggerView:selectedTypeForFormRequest:];
-[UIKBAutoFillTestGroundTruthGenerationViewController taggerView:selectedTypeForTextFieldRequest:];
-[UIKBAutoFillTestGroundTruthGenerationViewController taggerView:willTagRequest:];
-[UIKBAutoFillTestGroundTruthGenerationViewController taggerViewDidFinish:];
-[UIKBAutoFillTestGroundTruthGenerationViewController testViewController];
```
