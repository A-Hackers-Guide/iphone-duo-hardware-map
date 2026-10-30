# `EspressoDataFrame`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 7 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _inputAttachments;
@"NSMutableDictionary" _outputAttachments;
@"NSMutableDictionary" _groundTruthAttachments;
@"NSString" _function_name;
```

## Properties

```
@property (T@"NSMutableDictionary",&,V_inputAttachments) inputAttachments;
@property (T@"NSMutableDictionary",&,V_outputAttachments) outputAttachments;
@property (T@"NSMutableDictionary",&,V_groundTruthAttachments) groundTruthAttachments;
@property (T@"NSString",&,V_function_name) function_name;
@property (T@"NSArray",R) inputAttachmentNames;
@property (T@"NSArray",R) outputAttachmentNames;
@property (T@"NSArray",R) groundTruthAttachmentNames;
```

## Instance methods

```
-[EspressoDataFrame init];
-[EspressoDataFrame getFunctionName];
-[EspressoDataFrame function_name];
-[EspressoDataFrame getGroundTruthAttachment:];
-[EspressoDataFrame getInputAttachment:];
-[EspressoDataFrame getOutputAttachment:];
-[EspressoDataFrame groundTruthAttachmentNames];
-[EspressoDataFrame groundTruthAttachments];
-[EspressoDataFrame inputAttachmentNames];
-[EspressoDataFrame inputAttachments];
-[EspressoDataFrame loadFromDict:frameStorage:];
-[EspressoDataFrame outputAttachmentNames];
-[EspressoDataFrame outputAttachments];
-[EspressoDataFrame setFunction_name:];
-[EspressoDataFrame setGroundTruthAttachments:];
-[EspressoDataFrame setInputAttachments:];
-[EspressoDataFrame setOutputAttachments:];
```
