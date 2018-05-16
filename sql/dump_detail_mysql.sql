CREATE TABLE JobDetail(
  id INT NOT NULL AUTO_INCREMENT,
  latitude VARCHAR(15),
  longitude VARCHAR(15),
  advantage VARCHAR(501),
  positionName VARCHAR(30),
  experienceYear VARCHAR(30),
  address VARCHAR(200),
  education VARCHAR(30),
  salary VARCHAR(30),
  region VARCHAR(30),
  description VARCHAR(10001) NOT NULL,
  parttime VARCHAR(10),
  labels VARCHAR(501),
  title VARCHAR(501),
  keyword VARCHAR(200),
  job_id INT(11) DEFAULT NULL,
  PRIMARY KEY (id),
  CONSTRAINT refjobstb FOREIGN KEY (job_id) REFERENCES Jobs (id)
  )
ENGINE = InnoDB DEFAULT CHARSET=utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci;