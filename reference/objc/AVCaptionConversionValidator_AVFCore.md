# `AVCaptionConversionValidator`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 4 properties, 11 instance methods, 2 class methods

## Instance variables

```
^v _validatorInternal;
```

## Properties

```
@property (Tq,R) status;
@property (T@"NSArray",R) captions;
@property (T{?={?=qiIq}{?=qiIq}},R) timeRange;
@property (T@"NSArray",R) warnings;
```

## Class methods

```
+[AVCaptionConversionValidator captionConversionValidatorWithCaptions:timeRange:conversionSettings:];
+[AVCaptionConversionValidator mutableCaptionArray];
```

## Instance methods

```
-[AVCaptionConversionValidator timeRange];
-[AVCaptionConversionValidator dealloc];
-[AVCaptionConversionValidator status];
-[AVCaptionConversionValidator warnings];
-[AVCaptionConversionValidator _completeValidation];
-[AVCaptionConversionValidator _isConversionToClosedCaptions:];
-[AVCaptionConversionValidator _issueWarningForFigDictionary:];
-[AVCaptionConversionValidator captions];
-[AVCaptionConversionValidator initWithCaptions:timeRange:conversionSettings:];
-[AVCaptionConversionValidator stopValidating];
-[AVCaptionConversionValidator validateCaptionConversionWithWarningHandler:];
```
