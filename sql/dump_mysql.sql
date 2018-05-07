CREATE TABLE jobs (
  id INT NOT NULL AUTO_INCREMENT,
  businessZones VARCHAR(60),
  city VARCHAR(15),
  companyFullName VARCHAR(60),
  companyId INTEGER NOT NULL,
  companyLabelList VARCHAR(120),
  companyShortName VARCHAR(15),
  companySize VARCHAR(15),
  createTime DATE NOT NULL,
  district VARCHAR(15),
  education VARCHAR(30),
  explains VARCHAR(120),
  financeStage VARCHAR(15),
  firstType VARCHAR(60),
  secondType VARCHAR(60),
  formatCreateTime VARCHAR(15),
  gradeDescription VARCHAR(30),
  industryField VARCHAR(60),
  industryLables VARCHAR(120),
  jobNature VARCHAR(15),
  lastLogin TIMESTAMP,
  latitude VARCHAR(15),
  longitude VARCHAR(15),
  linestaion VARCHAR(120),
  stationname VARCHAR(30),
  subwayline VARCHAR(15),
  positionAdvantage VARCHAR(120),
  positionId INTEGER UNIQUE,
  positionLables VARCHAR(120),
  positionName VARCHAR(60),
  publisherId INTEGER NOT NULL,
  resumeProcessDay INTEGER,
  resumeProcessRate INTEGER,
  salary VARCHAR(60),
  score INTEGER,
  workYear VARCHAR(15),
  PRIMARY KEY (id),
  KEY idx_posid(positionId),
  KEY idx_sname(stationname),
  KEY idx_subw(subwayline)
  )
ENGINE = InnoDB;