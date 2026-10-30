# `SSREnrollmentUtterance`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 9 instance methods, 0 class methods

## Instance variables

```
B _isExplicit;
@"NSURL" _enrollmentUtteranceUrl;
Q _triggerPhrase;
@"NSDate" _approximateGenerationDate;
@"NSString" _productVersion;
@"NSString" _productType;
```

## Properties

```
@property (T@"NSURL",R,N,V_enrollmentUtteranceUrl) enrollmentUtteranceUrl;
@property (TB,R,N,V_isExplicit) isExplicit;
@property (TQ,R,N,V_triggerPhrase) triggerPhrase;
@property (T@"NSDate",R,N,V_approximateGenerationDate) approximateGenerationDate;
@property (T@"NSString",R,N,V_productVersion) productVersion;
@property (T@"NSString",R,N,V_productType) productType;
```

## Instance methods

```
-[SSREnrollmentUtterance productVersion];
-[SSREnrollmentUtterance productType];
-[SSREnrollmentUtterance description];
-[SSREnrollmentUtterance isExplicit];
-[SSREnrollmentUtterance triggerPhrase];
-[SSREnrollmentUtterance initWithEnrollmentUtteranceUrl:];
-[SSREnrollmentUtterance approximateGenerationDate];
-[SSREnrollmentUtterance enrollmentUtteranceUrl];
-[SSREnrollmentUtterance parseMetadataFromDictionary:];
```
