# `UIReferenceLibraryViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UITableViewDataSource`, `UITableViewDelegate`, `UINavigationControllerDelegate`
- 9 instance variables, 5 properties, 39 instance methods, 11 class methods

## Instance variables

```
@"NSString" _term;
@"NSArray" _definitionValues;
@"UINavigationController" _baseNavController;
@"UITableViewController" _multiDefViewController;
@"UIViewController" _longDefViewController;
q _oldPopoverStyle;
B _enableRotation;
B _previousIgnoreOrientation;
@? _dismissCompletionHandler;
```

## Properties

```
@property (T@?,C,N,V_dismissCompletionHandler) dismissCompletionHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIReferenceLibraryViewController _backgroundColor];
+[UIReferenceLibraryViewController _dictionaryDefinitionAttributes];
+[UIReferenceLibraryViewController dictionaryHasDefinitionForTerm:];
+[UIReferenceLibraryViewController _colorAttributes];
+[UIReferenceLibraryViewController _defaultButtonImage];
+[UIReferenceLibraryViewController _diddlyDoViewLineColor];
+[UIReferenceLibraryViewController _foregroundColor];
+[UIReferenceLibraryViewController _localizedDictionaryTitleAttributes];
+[UIReferenceLibraryViewController _pressedButtonImage];
+[UIReferenceLibraryViewController _shouldShowDefineForTerm:];
+[UIReferenceLibraryViewController _shouldShowDefineForTermOfLength:];
```

## Instance methods

```
-[UIReferenceLibraryViewController tableView:numberOfRowsInSection:];
-[UIReferenceLibraryViewController numberOfSectionsInTableView:];
-[UIReferenceLibraryViewController tableView:cellForRowAtIndexPath:];
-[UIReferenceLibraryViewController shouldAutorotateToInterfaceOrientation:];
-[UIReferenceLibraryViewController navigationController:willShowViewController:animated:];
-[UIReferenceLibraryViewController _backgroundColor];
-[UIReferenceLibraryViewController init];
-[UIReferenceLibraryViewController supportedInterfaceOrientations];
-[UIReferenceLibraryViewController tableView:titleForHeaderInSection:];
-[UIReferenceLibraryViewController viewDidLoad];
-[UIReferenceLibraryViewController _didResignContentViewControllerOfPopover:];
-[UIReferenceLibraryViewController shouldAutorotate];
-[UIReferenceLibraryViewController _willBecomeContentViewControllerOfPopover:];
-[UIReferenceLibraryViewController initWithNibName:bundle:];
-[UIReferenceLibraryViewController tableView:heightForRowAtIndexPath:];
-[UIReferenceLibraryViewController tableView:willSelectRowAtIndexPath:];
-[UIReferenceLibraryViewController viewWillLayoutSubviews];
-[UIReferenceLibraryViewController initWithCoder:];
-[UIReferenceLibraryViewController _dictionaryDefinitionAttributes];
-[UIReferenceLibraryViewController _colorAttributes];
-[UIReferenceLibraryViewController _defaultButtonImage];
-[UIReferenceLibraryViewController _diddlyDoViewLineColor];
-[UIReferenceLibraryViewController _dismissModalReferenceView:];
-[UIReferenceLibraryViewController _foregroundColor];
-[UIReferenceLibraryViewController _installDoneButtonOnViewControllerIfNeeded:];
-[UIReferenceLibraryViewController _installRequiredElementsOnViewController:];
-[UIReferenceLibraryViewController _localizedDictionaryTitleAttributes];
-[UIReferenceLibraryViewController _preferredInterfaceOrientationGivenCurrentOrientation:];
-[UIReferenceLibraryViewController _pressedButtonImage];
-[UIReferenceLibraryViewController _searchWeb:];
-[UIReferenceLibraryViewController _semanticContextTraitChanged];
-[UIReferenceLibraryViewController _setPopoverController:];
-[UIReferenceLibraryViewController dismissCompletionHandler];
-[UIReferenceLibraryViewController enableRotation];
-[UIReferenceLibraryViewController initWithTerm:];
-[UIReferenceLibraryViewController pushDownloadManager:];
-[UIReferenceLibraryViewController setDismissCompletionHandler:];
-[UIReferenceLibraryViewController setEnableRotation:];
-[UIReferenceLibraryViewController window:setupWithInterfaceOrientation:];
```
