# `UIStoryboard`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 11 properties, 30 instance methods, 1 class methods

## Instance variables

```
@"NSBundle" bundle;
@"NSString" storyboardFileName;
@"NSDictionary" identifierToNibNameMap;
@"NSDictionary" identifierToExternalStoryboardReferenceMap;
@"NSString" designatedEntryPointIdentifier;
@"NSString" designatedMenuIdentifier;
@"NSMutableDictionary" identifierToUINibMap;
@"UIStoryboardSegueTemplate" ___currentStoryboardSegueTemplate;
@? ___currentStoryboardSegueCreator;
@ ___currentSender;
```

## Properties

```
@property (T@"NSString",R,N,VstoryboardFileName) storyboardFileName;
@property (T@"NSDictionary",R,N,VidentifierToNibNameMap) identifierToNibNameMap;
@property (T@"NSDictionary",R,N,VidentifierToExternalStoryboardReferenceMap) identifierToExternalStoryboardReferenceMap;
@property (T@"NSString",R,N,VdesignatedEntryPointIdentifier) designatedEntryPointIdentifier;
@property (T@"NSString",R,N,VdesignatedMenuIdentifier) designatedMenuIdentifier;
@property (T@"NSMutableDictionary",R,N,VidentifierToUINibMap) identifierToUINibMap;
@property (T@"UIStoryboardSegueTemplate",N,V___currentStoryboardSegueTemplate) __currentStoryboardSegueTemplate;
@property (T@?,N,V___currentStoryboardSegueCreator) __currentStoryboardSegueCreator;
@property (T@,N,V___currentSender) __currentSender;
@property (T@"NSBundle",R,N,Vbundle) bundle;
@property (T@"NSString",R) name;
```

## Class methods

```
+[UIStoryboard storyboardWithName:bundle:];
```

## Instance methods

```
-[UIStoryboard bundle];
-[UIStoryboard dealloc];
-[UIStoryboard identifierForStringsFile];
-[UIStoryboard name];
-[UIStoryboard __currentSender];
-[UIStoryboard __currentStoryboardSegueCreator];
-[UIStoryboard __currentStoryboardSegueTemplate];
-[UIStoryboard __reallyInstantiateViewControllerWithIdentifier:creator:storyboardSegueTemplate:sender:];
-[UIStoryboard _instantiateInitialMenu];
-[UIStoryboard _instantiateInitialViewControllerWithCreator:storyboardSegueTemplate:sender:];
-[UIStoryboard _instantiateViewControllerReferencedByPlaceholderWithIdentifier:storyboardSegueTemplate:sender:];
-[UIStoryboard _instantiateViewControllerWithIdentifier:creator:storyboardSegueTemplate:sender:];
-[UIStoryboard containsNibNamed:];
-[UIStoryboard designatedEntryPointIdentifier];
-[UIStoryboard designatedMenuIdentifier];
-[UIStoryboard identifierToExternalStoryboardReferenceMap];
-[UIStoryboard identifierToNibNameMap];
-[UIStoryboard identifierToUINibMap];
-[UIStoryboard initWithBundle:storyboardFileName:identifierToNibNameMap:identifierToExternalStoryboardReferenceMap:designatedEntryPointIdentifier:designatedMenuIdentifier:];
-[UIStoryboard instantiateInitialViewController];
-[UIStoryboard instantiateInitialViewControllerWithCreator:];
-[UIStoryboard instantiateViewControllerWithIdentifier:];
-[UIStoryboard instantiateViewControllerWithIdentifier:creator:];
-[UIStoryboard nibForStoryboardNibNamed:];
-[UIStoryboard nibForViewControllerWithIdentifier:];
-[UIStoryboard referencedStoryboardForExternalReferenceInfo:];
-[UIStoryboard set__currentSender:];
-[UIStoryboard set__currentStoryboardSegueCreator:];
-[UIStoryboard set__currentStoryboardSegueTemplate:];
-[UIStoryboard storyboardFileName];
```
