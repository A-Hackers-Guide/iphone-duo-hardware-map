# `SSRVoiceProfile`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 15 instance variables, 24 properties, 77 instance methods, 1 class methods

## Instance variables

```
@"NSString" _locale;
@"NSString" _appDomain;
@"NSDate" _dateAdded;
@"NSString" _profileID;
@"NSString" _siriProfileId;
@"NSString" _enrollmentId;
@"NSString" _personaID;
@"NSNumber" _profilePitch;
@"NSString" _profileBasePath;
@"NSString" _profileBasePathExclave;
@"NSMutableArray" _donationIds;
@"NSArray" _enrollmentSNR;
@"NSArray" _enrollmentWER;
@"NSArray" _enrollmentSimilarityScores;
@"NSString" _userName;
```

## Properties

```
@property (T@"NSString",&,N,V_profileBasePath) profileBasePath;
@property (T@"NSString",&,N,V_profileBasePathExclave) profileBasePathExclave;
@property (T@"NSMutableArray",&,N,V_donationIds) donationIds;
@property (T@"NSArray",&,N,V_enrollmentSNR) enrollmentSNR;
@property (T@"NSArray",&,N,V_enrollmentWER) enrollmentWER;
@property (T@"NSArray",&,N,V_enrollmentSimilarityScores) enrollmentSimilarityScores;
@property (T@"NSString",R,N) voiceProfileBasePath;
@property (T@"NSString",R,N) voiceProfileImplicitCacheDirPath;
@property (T@"NSString",R,N) voiceProfileIdentity;
@property (TQ,R,N) voiceProfileVersion;
@property (TQ,R,N) productCategory;
@property (T@"NSString",R,N) pruningCookie;
@property (TB,R,N) profileLocallyAvailable;
@property (T@"NSString",&,N,V_userName) userName;
@property (T@"NSString",R,N,V_locale) locale;
@property (T@"NSString",R,N,V_appDomain) appDomain;
@property (T@"NSDate",R,N,V_dateAdded) dateAdded;
@property (T@"NSString",R,N,V_profileID) profileID;
@property (T@"NSString",R,N,V_siriProfileId) siriProfileId;
@property (T@"NSString",R,N,V_enrollmentId) enrollmentId;
@property (T@"NSString",R,N,V_personaID) personaID;
@property (T@"NSArray",R,N) tdtiEnrollmentUtterances;
@property (T@"NSArray",R,N) tdEnrollmentUtterances;
@property (T@"NSNumber",&,N,V_profilePitch) profilePitch;
```

## Class methods

```
+[SSRVoiceProfile supportsSecureCoding];
```

## Instance methods

```
-[SSRVoiceProfile personaID];
-[SSRVoiceProfile userName];
-[SSRVoiceProfile initWithDictionary:];
-[SSRVoiceProfile setPersonaId:];
-[SSRVoiceProfile dateAdded];
-[SSRVoiceProfile locale];
-[SSRVoiceProfile encodeWithCoder:];
-[SSRVoiceProfile description];
-[SSRVoiceProfile initWithCoder:];
-[SSRVoiceProfile profileID];
-[SSRVoiceProfile productCategory];
-[SSRVoiceProfile dictionaryRepresentation];
-[SSRVoiceProfile setUserName:];
-[SSRVoiceProfile enrollmentId];
-[SSRVoiceProfile appDomain];
-[SSRVoiceProfile siriProfileId];
-[SSRVoiceProfile profileBasePath];
-[SSRVoiceProfile setDonationIds:];
-[SSRVoiceProfile getTDAudioCount];
-[SSRVoiceProfile _copyExplicitAudio:withSpIdType:];
-[SSRVoiceProfile _getEnrollmentUtterancesForType:];
-[SSRVoiceProfile _getProfileVersionFilePath];
-[SSRVoiceProfile _isSATMarkedWithMarker:];
-[SSRVoiceProfile _markSATEnrollmentWithMarker:];
-[SSRVoiceProfile _updateVoiceProfileVersionFile];
-[SSRVoiceProfile _voiceProfilePathForSpidType:];
-[SSRVoiceProfile addDonationId:];
-[SSRVoiceProfile addEnrollmentSNR:];
-[SSRVoiceProfile addEnrollmentSimilarityScore:];
-[SSRVoiceProfile addEnrollmentWER:];
-[SSRVoiceProfile addUtterances:spIdType:];
-[SSRVoiceProfile copyTDAudioToTDTI];
-[SSRVoiceProfile deleteModelForSpidType:recognizerType:];
-[SSRVoiceProfile donationIds];
-[SSRVoiceProfile enrollmentSNR];
-[SSRVoiceProfile enrollmentSimilarityScores];
-[SSRVoiceProfile enrollmentWER];
-[SSRVoiceProfile exclaveVoiceProfileModelFilePathForRecognizerType:spIdType:];
-[SSRVoiceProfile getDonationIds];
-[SSRVoiceProfile getEnrollmentSNR];
-[SSRVoiceProfile getEnrollmentSimilarityScores];
-[SSRVoiceProfile getEnrollmentUtterancesForModelType:];
-[SSRVoiceProfile getEnrollmentWER];
-[SSRVoiceProfile getExplicitEnrollmentUtterancesForType:];
-[SSRVoiceProfile getExplicitMarkedEnrollmentUtterancesForType:];
-[SSRVoiceProfile getImplicitEnrollmentUtterancesForType:];
-[SSRVoiceProfile getImplicitEnrollmentUtterancesPriorTo:forType:];
-[SSRVoiceProfile importVoiceProfileAtPath:];
-[SSRVoiceProfile initNewVoiceProfileWithLocale:withAppDomain:];
-[SSRVoiceProfile isMarkedSATEnrolled];
-[SSRVoiceProfile isMarkedSATMigrated];
-[SSRVoiceProfile isValidForRPIWithError:];
-[SSRVoiceProfile markSATEnrollmentMigrated];
-[SSRVoiceProfile markSATEnrollmentSuccess];
-[SSRVoiceProfile profileBasePathExclave];
-[SSRVoiceProfile profileLocallyAvailable];
-[SSRVoiceProfile profilePitch];
-[SSRVoiceProfile pruningCookie];
-[SSRVoiceProfile setEnrollmentSNR:];
-[SSRVoiceProfile setEnrollmentSimilarityScores:];
-[SSRVoiceProfile setEnrollmentWER:];
-[SSRVoiceProfile setProfileBasePath:];
-[SSRVoiceProfile setProfileBasePathExclave:];
-[SSRVoiceProfile setProfilePitch:];
-[SSRVoiceProfile setSharedSiriProfileId:];
-[SSRVoiceProfile tdEnrollmentUtterances];
-[SSRVoiceProfile tdtiEnrollmentUtterances];
-[SSRVoiceProfile updatePruningCookie:];
-[SSRVoiceProfile updateVoiceProfilePathExclave:];
-[SSRVoiceProfile voiceProfileAudioDirPathForSpidType:];
-[SSRVoiceProfile voiceProfileBasePath];
-[SSRVoiceProfile voiceProfileIdentity];
-[SSRVoiceProfile voiceProfileImplicitCacheDirPath];
-[SSRVoiceProfile voiceProfileModelDirForSpidType:recognizerType:];
-[SSRVoiceProfile voiceProfileModelFilePathForRecognizerType:spIdType:];
-[SSRVoiceProfile voiceProfilePathExclave];
-[SSRVoiceProfile voiceProfileVersion];
```
