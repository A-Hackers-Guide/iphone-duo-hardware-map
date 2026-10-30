# `UITextPasteItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UITextPasteItem`
- 7 instance variables, 11 properties, 21 instance methods, 0 class methods

## Instance variables

```
B _forcesDefaultAttributes;
@"NSItemProvider" _itemProvider;
@ _localObject;
@"NSDictionary" _defaultAttributes;
@"UITextPasteCoordinator" _coordinator;
@"NSArray" _supportedPasteConfigurationClasses;
@"NSDictionary" _documentOptions;
```

## Properties

```
@property (T@"NSItemProvider",&,N,V_itemProvider) itemProvider;
@property (T@,&,N,V_localObject) localObject;
@property (T@"NSDictionary",&,N,V_defaultAttributes) defaultAttributes;
@property (T@"UITextPasteCoordinator",R,N,V_coordinator) coordinator;
@property (T@"NSArray",&,N,V_supportedPasteConfigurationClasses) supportedPasteConfigurationClasses;
@property (TB,N,V_forcesDefaultAttributes) forcesDefaultAttributes;
@property (T@"NSDictionary",C,N,V_documentOptions) documentOptions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UITextPasteItem setDefaultAttributes:];
-[UITextPasteItem defaultAttributes];
-[UITextPasteItem setLocalObject:];
-[UITextPasteItem localObject];
-[UITextPasteItem itemProvider];
-[UITextPasteItem coordinator];
-[UITextPasteItem documentOptions];
-[UITextPasteItem attributedStringFromAttributedString:preservingAttributes:addingAttributes:];
-[UITextPasteItem attributesWithContentAwareWritingDirectionForString:defaultAttributes:];
-[UITextPasteItem forcesDefaultAttributes];
-[UITextPasteItem initWithTextPasteCoordinator:];
-[UITextPasteItem setAttachmentResult:];
-[UITextPasteItem setAttributedStringResult:];
-[UITextPasteItem setDefaultResult];
-[UITextPasteItem setDocumentOptions:];
-[UITextPasteItem setForcesDefaultAttributes:];
-[UITextPasteItem setItemProvider:];
-[UITextPasteItem setNoResult];
-[UITextPasteItem setStringResult:];
-[UITextPasteItem setSupportedPasteConfigurationClasses:];
-[UITextPasteItem supportedPasteConfigurationClasses];
```
