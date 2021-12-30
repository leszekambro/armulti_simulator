; Auto-generated. Do not edit!


(cl:in-package inz-msg)


;//! \htmlinclude PoseTwist.msg.html

(cl:defclass <PoseTwist> (roslisp-msg-protocol:ros-message)
  ((position_x
    :reader position_x
    :initarg :position_x
    :type cl:float
    :initform 0.0)
   (position_y
    :reader position_y
    :initarg :position_y
    :type cl:float
    :initform 0.0)
   (position_z
    :reader position_z
    :initarg :position_z
    :type cl:float
    :initform 0.0)
   (velocity_x
    :reader velocity_x
    :initarg :velocity_x
    :type cl:float
    :initform 0.0)
   (velocity_y
    :reader velocity_y
    :initarg :velocity_y
    :type cl:float
    :initform 0.0)
   (velocity_z
    :reader velocity_z
    :initarg :velocity_z
    :type cl:float
    :initform 0.0))
)

(cl:defclass PoseTwist (<PoseTwist>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PoseTwist>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PoseTwist)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name inz-msg:<PoseTwist> is deprecated: use inz-msg:PoseTwist instead.")))

(cl:ensure-generic-function 'position_x-val :lambda-list '(m))
(cl:defmethod position_x-val ((m <PoseTwist>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader inz-msg:position_x-val is deprecated.  Use inz-msg:position_x instead.")
  (position_x m))

(cl:ensure-generic-function 'position_y-val :lambda-list '(m))
(cl:defmethod position_y-val ((m <PoseTwist>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader inz-msg:position_y-val is deprecated.  Use inz-msg:position_y instead.")
  (position_y m))

(cl:ensure-generic-function 'position_z-val :lambda-list '(m))
(cl:defmethod position_z-val ((m <PoseTwist>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader inz-msg:position_z-val is deprecated.  Use inz-msg:position_z instead.")
  (position_z m))

(cl:ensure-generic-function 'velocity_x-val :lambda-list '(m))
(cl:defmethod velocity_x-val ((m <PoseTwist>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader inz-msg:velocity_x-val is deprecated.  Use inz-msg:velocity_x instead.")
  (velocity_x m))

(cl:ensure-generic-function 'velocity_y-val :lambda-list '(m))
(cl:defmethod velocity_y-val ((m <PoseTwist>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader inz-msg:velocity_y-val is deprecated.  Use inz-msg:velocity_y instead.")
  (velocity_y m))

(cl:ensure-generic-function 'velocity_z-val :lambda-list '(m))
(cl:defmethod velocity_z-val ((m <PoseTwist>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader inz-msg:velocity_z-val is deprecated.  Use inz-msg:velocity_z instead.")
  (velocity_z m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PoseTwist>) ostream)
  "Serializes a message object of type '<PoseTwist>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'position_x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'position_y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'position_z))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'velocity_x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'velocity_y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'velocity_z))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PoseTwist>) istream)
  "Deserializes a message object of type '<PoseTwist>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'position_x) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'position_y) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'position_z) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'velocity_x) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'velocity_y) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'velocity_z) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PoseTwist>)))
  "Returns string type for a message object of type '<PoseTwist>"
  "inz/PoseTwist")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PoseTwist)))
  "Returns string type for a message object of type 'PoseTwist"
  "inz/PoseTwist")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PoseTwist>)))
  "Returns md5sum for a message object of type '<PoseTwist>"
  "6a09e933f209950ba0d299b5621ed0ec")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PoseTwist)))
  "Returns md5sum for a message object of type 'PoseTwist"
  "6a09e933f209950ba0d299b5621ed0ec")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PoseTwist>)))
  "Returns full string definition for message of type '<PoseTwist>"
  (cl:format cl:nil "float32 position_x~%float32 position_y~%float32 position_z~%float32 velocity_x~%float32 velocity_y~%float32 velocity_z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PoseTwist)))
  "Returns full string definition for message of type 'PoseTwist"
  (cl:format cl:nil "float32 position_x~%float32 position_y~%float32 position_z~%float32 velocity_x~%float32 velocity_y~%float32 velocity_z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PoseTwist>))
  (cl:+ 0
     4
     4
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PoseTwist>))
  "Converts a ROS message object to a list"
  (cl:list 'PoseTwist
    (cl:cons ':position_x (position_x msg))
    (cl:cons ':position_y (position_y msg))
    (cl:cons ':position_z (position_z msg))
    (cl:cons ':velocity_x (velocity_x msg))
    (cl:cons ':velocity_y (velocity_y msg))
    (cl:cons ':velocity_z (velocity_z msg))
))
