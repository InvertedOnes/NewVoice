U
    �k�^�  �                B   @   s�  d dl Z d dlZd dlZe �d� edd�Ze��  dZdd� Zdd	� Z	e
d
� ed�Zedk�r�ed�Z�zejed�Zejeddd�Zee	dddddddddddddddddddddddddddddd d!g�� ee	ddddd"dd#d#dd$ddddddddddddd dd"dddd%dd&d'd(d)d*d+d,d-d.d-d/d)d0ddddd%dd&d'd-d0dddddddd'dd1d!g@�� edd2�Ze�ed3 � e��  W n   e
d4� Y nX e
�  e�  ned5k�r�e
d6� e�  e
�  edd7�Ze�� Ze��  eee��D ]xZee dd8� ee< ejee d�Zejed9dd�Zej�� d  Zed: d; ed<  Ze
d=e d> eed? � � �q�eeed@��d?  Zejed�Zejed9dd�Ze� Z ee d? �Z!e
�  g Z"e �#e�D ]>Z$e$dAd� dBk�r�e"�%e$� e
d=e$ d> eee"�� � �q�ee"eed@��d?   Z&ej'j(dCe!dD�dE Z)ej*e)dFee&dG�idH��+� Z,ej'j-e,dF dIdJ�d  Z$dKee$dL � dM ee$dN � Z.ej/j0e!e.dO� e
dP� dS )Q�    N�clearz.tokensza+z/storage/emulated/0/Download/c                  C   s  d} d}d}d}d}t d�}tt|��D ]�}|| dkr@|d } || k rJq(|dkr�| dkr�z4|| dkrp|d7 }t|| � d}||| 7 }W q�   ||| 7 }Y q�X q(|dkr�|| dkr�||| 7 }q�d	}q(|d	kr(||| 7 }q(|dk�rtd
� t�  n|d dk�rd}|||fS )Nr   � z[35mEnter the link: [0m�.�   �-�   �_�   z
[31mInvalid link
�w�post)�input�range�len�int�print�quit)Zspace�step�typeZfirstIDZsecondID�link�char� r   �voice.py�getlink
   sB    
r   c                 C   s*   d}| D ]}|t t|d d ��7 }q|S )Nr   �   g      �?)�chrr   )Zmassive�str�nr   r   r   �dec.   s    r   ut  [37m
 InvertedOnes                           Vk: @inv_ones[32m
 ┏━┳━━━┳━━━━━┳━┳━┳━┓  ┏━━┳━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┓
 ┃ ┃   ┃  ━━━┫ ┃ ┃ ┃  ┃  ┃  ┃  ┓  ┣━┓ ┏━┫ ┏━━━┫  ━━━┫
 ┃   ┃ ┃  ━━━┫     ┃  ┗┓   ┏┫  ┗  ┣━┛ ┗━┫ ┗━━━┫  ━━━┫
 ┗━━━┻━┻━━━━━┻━━┻━━┛   ┗━━━┛┗━━━━━┻━━━━━┻━━━━━┻━━━━━┛
[35m
[1] Send voice
[2] Add token
z&Please, enter your task's number: [0m�2z[35mEnter the token: [0m)Zaccess_tokenz5.92Zru)�vZlangi�$  i1  i+  iP  iu.  i�'  i�3  i})  i�4  i�  i-0  iP/  ip6  i�2  iL  i�  i]7  i�-  iU&  iM#  i'  i�  i�  im	  i�  i  iL  i�	  ip  i	  i�  i�,  �a�
z
[31mInvalid token�1z
[31mInvalid task number
�r�����z5.89Z
first_name� �	last_namez[33mz[37m r   z
[35mYour choice: [0m�����z.oggZaudio_message)r   Zpeer_idZ
upload_url�file�rb)�fileszIt's me)r(   �title�docZowner_idr   �id)Zuser_id�
attachmentz
[32mSuccessful
)1�osZvkZrequests�system�open�f�close�pathr   r   r   r   ZtaskZtkZSessionZsessionZAPIZapi�execr
   �writer   �	readlines�tokensr   r   Zusers�get�userr   r   �tokenZ	parametrsZ	recipientZaudios�listdirr(   �appendZaudioZdocsZgetMessagesUploadServerr   r   ZjsonZresponseZsaver.   Zmessages�sendr   r   r   r   �<module>   sl   

$
J�


 
  